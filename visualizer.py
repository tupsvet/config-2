import argparse
import os
import gzip
import requests
import subprocess

def download_and_extract_packages(repo_url, output_file):
    packages_url = f"{repo_url}/Packages.gz"
    print(f"Downloading {packages_url}")
    
    response = requests.get(packages_url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download {packages_url}")
    
    with open(output_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    extracted_file = output_file.replace(".gz", "")
    
    with gzip.open(output_file, 'rb') as gz_file:
        with open(extracted_file, 'wb') as f: 
            f.write(gz_file.read()) 

    print(f"Extracted to {extracted_file}")
    return extracted_file

def parse_packages_file(packages_file):
    packages = {}
    current_package = None
    dependencies = None

    with open(packages_file, 'r', encoding='utf-8') as f:  # Явное указание кодировки UTF-8
        for line in f:
            line = line.strip()
            if line.startswith("Package:"):
                current_package = line.split(":")[1].strip()
            elif line.startswith("Depends:"):
                dependencies = line.split(":")[1].strip()
            elif line == "" and current_package:
                # Если зависимости указаны, разделяем их по ", "
                packages[current_package] = dependencies.split(", ") if dependencies else []
                current_package = None
                dependencies = None

    return packages

def get_dependencies(package, packages, package_dict, depth, max_depth):
    if package in package_dict or (max_depth is not None and depth > max_depth):
        return package_dict.get(package, [])

    if package not in packages:
        return []

    print(f"Analyzing {package}")
    dependencies = packages[package]
    package_dict[package] = dependencies
    for dep in dependencies:
        get_dependencies(dep, packages, package_dict, depth + 1, max_depth)
    return dependencies


def generate_graph_code(package_dict):
    res = 'flowchart TD;\n'
    cnt = 0
    ids = {}

    for key in package_dict.keys():
        if package_dict[key] is None:
            continue
        if key in ids:
            cur_id = ids[key]
        else:
            cur_id = f'id{cnt}'
            ids[key] = cur_id
            cnt += 1
        for dep in package_dict[key]:
            if dep in ids:
                dep_id = ids[dep]
            else:
                dep_id = f'id{cnt}'
                ids[dep] = dep_id
                cnt += 1
            res += f'\t{cur_id}["{key}"] --> {dep_id}["{dep}"];\n'
    return res


def main():
    parser = argparse.ArgumentParser(description="Visualize package dependencies.")
    parser.add_argument('--path', type=str, required=True, help='Path to the mermaid CLI')
    parser.add_argument('--package', type=str, required=True, help='Package name')
    parser.add_argument('--repo', type=str, required=True, help='Repository base URL')
    parser.add_argument('--output', type=str, default=None, help='Output file for the SVG')
    parser.add_argument('--max-depth', type=int, default=None, help='Max depth for dependency analysis')
    args = parser.parse_args()

    repo = args.repo
    package = args.package
    output_file = args.output or f'{package}_output.svg'
    packages_file = "Packages.gz"
    
    extracted_file = download_and_extract_packages(repo, packages_file)

    print("Parsing Packages file...")
    packages = parse_packages_file(extracted_file)

    print("Building dependency tree...")
    package_dict = {}
    get_dependencies(package, packages, package_dict, depth=0, max_depth=args.max_depth)

    graph = generate_graph_code(package_dict)
    graph_file = f'{package}_graph_code.mmd'
    with open(graph_file, 'w') as f:
        f.write(graph)
    print(f"Graph code saved to {os.path.abspath(graph_file)}")

    subprocess.run([args.path, "C:\\Users\\kolos\\AppData\\Roaming\\npm\\node_modules\\@mermaid-js\\mermaid-cli\\src\\cli.js" , "-i", graph_file, "-o", output_file], shell=False, check=True)
    print(f"Visualization saved to {os.path.abspath(output_file)}")


if __name__ == "__main__":
    main()