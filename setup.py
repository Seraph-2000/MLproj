from setuptools import find_packages,setup
from typing import List

hed = '-e .'
def get_requirements(file_path:str)->List[str]:
    #This function will return a list of required packages
    req=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hed in requirements:
            requirements.remove(hed)
    return requirements


setup(
name="ML-project",
version="0.0.1",
author="Kunal",
author_email="santkunal2000@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt"),

)


