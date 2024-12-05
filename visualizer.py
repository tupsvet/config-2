import argparse
import os
import subprocess
import requests
from bs4 import BeautifulSoup
from xml.dom import minidom


def get_package_meta_url(pack_url):
    response = requests.get(pack_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and not href.startswith('?') and '.dsc' in href:
                return pack_url + href
        return None
    print(f'!----Cant reach {pack_url} ----!')
    return None


def get_dependency_text(description):
    dependency_flag = 'Build-Depends:'
    alt = 'Build-Depends-Indep:'

    for line in description.splitlines():
        if dependency_flag in line:
            return line[len(dependency_flag):].replace(' ', '')
        if alt in line:
            return line[len(alt):].replace(' ', '')
    return None


def trim_package(package):
    for i in range(len(package)):
        if package[i] in '(){}[]>=<.':
            return package[:i]
    return package


def extract_dependencies(dependency_text):
    return dependency_text.split(',')


def get_dependencies(repo, package, package_dict, depth, max_depth):
    if package in package_dict or (max_depth is not None and depth > max_depth):
        return package_dict.get(package, [])
    trimed = trim_package(package)
    url = f"{repo}{trimed[:4] if 'lib' in package else trimed[0]}/{trimed}/"
    desc_url = get_package_meta_url(url)
    if desc_url is None:
        return []

    print(f'Analyzing {package}')
    response = requests.get(desc_url)
    dependencies = extract_dependencies(get_dependency_text(response.text))
    package_dict[package] = dependencies
    for dep in dependencies:
        package_dict[dep] = get_dependencies(repo, dep, package_dict, depth + 1, max_depth)
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


def beautify_svg(svg_file):
    with open(svg_file, 'r') as f:
        svg_content = f.read()
    dom = minidom.parseString(svg_content)
    return dom.toprettyxml()


def main():
    parser = argparse.ArgumentParser(description="Visualize package dependencies.")
    parser.add_argument('--path', type=str, required=True, help='Path to the mermaid CLI')
    parser.add_argument('--package', type=str, required=True, help='Package name')
    parser.add_argument('--repo', type=str, required=True, help='Repository URL')
    parser.add_argument('--output', type=str, default=None, help='Output file for the SVG')
    parser.add_argument('--max-depth', type=int, default=None, help='Max depth for dependency analysis')
    args = parser.parse_args()

    path = args.path
    package = args.package
    repo = args.repo
    output_file = args.output or f'{package}_output.svg'

    print(f'Visualization started with params:\npath: {path}\npackage: {package}\nrepo: {repo}\noutput: {output_file}\n')

    package_dict = {}
    print('Dependencies will only be displayed for packages that have .dsc file in their repo!')
    dependencies = get_dependencies(repo, package, package_dict, depth=0, max_depth=args.max_depth)

    print('Dependency tree created. Starting generating graph code')
    graph = generate_graph_code(package_dict)
    graph_file = f'{package}_graph_code.mmd'
    with open(graph_file, 'w') as f:
        f.write(graph)
    print(f'Graph code saved in {os.path.abspath(graph_file)}')

    subprocess.run([path,"C:\\Users\\kolos\\AppData\\Roaming\\npm\\node_modules\\@mermaid-js\\mermaid-cli\\src\\cli.js", "-i", graph_file, "-o", output_file], shell=False, check=True)

    print("\nSVG content:")
    beautified_svg = beautify_svg(output_file)
    print(beautified_svg)

    print(f'Visualization saved in {os.path.abspath(output_file)}')


if __name__ == "__main__":
    main()