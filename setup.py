from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
    # Remove any leading/trailing whitespace characters and filter out empty lines
    requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='MLProject',
    version='0.1.0',
    author='Naman',
    author_email = "nkhmtwtfss@gmail.com",
    install_requires=get_requirements('requirements.txt'),
)