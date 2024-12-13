import pytest
from unittest.mock import patch, MagicMock
import os
from visualizer import *

@patch('requests.get')
@patch('gzip.open')
@patch('builtins.open')
def test_download_and_extract_packages(mock_open, mock_gzip, mock_requests):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.iter_content = MagicMock(return_value=[b'fake data'])
    mock_requests.return_value = mock_response

    mock_file = MagicMock()
    mock_open.return_value = mock_file
    mock_gzip.return_value = MagicMock(read=MagicMock(return_value=b'fake decompressed data'))

    repo_url = "http://archive.ubuntu.com/ubuntu/dists/focal/main/binary-amd64"
    output_file = "Packages.gz"
    
    extracted_file = download_and_extract_packages(repo_url, output_file)
    
    mock_requests.assert_called_once_with(f"{repo_url}/Packages.gz", stream=True)
    mock_open.assert_called_with('Packages', 'wb')  
    mock_gzip.assert_called_once()  
    assert extracted_file == "Packages"  

def test_parse_packages_file():
    packages_file = "Packages"
    with open(packages_file, 'w', encoding='utf-8') as f:
        f.write("Package: lib1\nDepends: lib2, lib3\n\n")
        f.write("Package: lib2\nDepends: lib4\n\n")
    
    packages = parse_packages_file(packages_file)
    
    assert packages == {
        "lib1": ["lib2", "lib3"],
        "lib2": ["lib4"]
    }
    
    os.remove(packages_file)

def test_get_dependencies():
    packages = {
        "lib1": ["lib2", "lib3"],
        "lib2": ["lib4"],
        "lib3": [],
        "lib4": ["lib5"]
    }
    package_dict = {}
    repo = "http://archive.ubuntu.com/ubuntu/dists/focal/main"
    package = "lib1"
    
    dependencies = get_dependencies(package, packages, package_dict, depth=0, max_depth=None)
    
    assert dependencies == ["lib2", "lib3"]
    
    assert package_dict == {
        "lib1": ["lib2", "lib3"],
        "lib2": ["lib4"],
        "lib3": [],
        "lib4": ["lib5"]
    }
