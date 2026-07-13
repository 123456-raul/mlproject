from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="my_package",
    version="0.1.0",
    author="Rahul",
    author_email="<rahul9554781945@gmail.com>",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")




)