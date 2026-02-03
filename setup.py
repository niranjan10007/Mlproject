from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements from a requirements.txt file
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # remove newlines and spaces
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',                         # Project name
    version='0.0.1',                          # Version
    author='Niranjan',                        # Your name
    author_email='niranjanbarhate058@gmail.com', # Your email
    packages=find_packages(),                 # Include all packages in the folder
    install_requires=get_requirements('requirements.txt')  # Dependencies
)
