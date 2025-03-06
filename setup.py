from setuptools import find_packages, setup

setup(
    name='chicken disease classification',
    version='0.0.0',
    author='mohammed arif',
    author_email="mohammedarifsn2@gmail.com",
    description="A small python package for CNN app",
    url="https://github.com/mohammedarifsn12",
    project_urls="https://github.com/mohammedarifsn12/chicken-disease-classification",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)