from setuptools import setup, find_packages
from typing import List



def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of packages.
    Ignores empty lines, comments, and editable installs (-e).
    """
    requirement_list: List[str] = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                requirement = line.strip()
                if requirement and not requirement.startswith('#') and not requirement.startswith('-e'):
                    requirement_list.append(requirement)
        print(f"Requirements loaded from {file_path}: {requirement_list}")
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Returning an empty list.")
        return []

    return requirement_list


setup(
    name='NetworkSecurity',
    version='0.1.0',
    author='Ashok',
    description='A package for network security analysis and tools.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
