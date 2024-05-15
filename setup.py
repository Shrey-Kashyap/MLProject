from setuptools import find_packages,setup

DASH_E_DOT="-e ."
def get_requirements(file):
    with open(file, 'r') as f:
        requirements=f.readlines()
    
    requirements = [_.replace("\n","") for _ in requirements]
    requirements.remove(DASH_E_DOT)

    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="Shrey",
    author_email="kashyap.shrey.2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
