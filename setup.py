from gettext import install
from setuptools import find_packages,setup
from typing import List

hypen="-e."

def get_requirments(file_path:str)->List[str]: #takes requirment.txt and return list of string from file
    "returns list of requirment"
    requirment=[]

    with open(file_path) as f:
        requirment=f.readlines()        #read every line ..... 
        requirment=[i.replace("/n","") for i in requirment]         #to ignore /n(ends with /n for next line)
        if hypen in requirment:
            requirment.remove(hypen)
    
    return requirment

setup(
    name="ds",
    packages=find_packages(),
    install_requires=get_requirments("requirments.txt")
)