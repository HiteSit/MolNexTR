from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='MolNexTR',
    version='0.1',
    author='NOT-HiteSit',
    description='MolNexTR: A novel graph generation model for molecular structure recognition.',
    packages=find_packages(),
    install_requires=requirements,
)
