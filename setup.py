 
from typing import List
from setuptools import setup, find_packages

PROJECT_NAME='HOUSING PREDITOR'
VERSION ='.0.2'
DESCRIPTION='THIS IS FOR HOUSING'
PACKAGES=['housing']
AUTHER='DAYA'
REQUIREMENT_FILE='requirements.txt'

def get_requirementList()-> List[str]:
    open('requirements.txt','r').readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHER,
    packages=find_packages(), ##PACKAGES,
    install_requires=get_requirementList()
    )

 
