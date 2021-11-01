from setuptools import setup, find_packages

setup (
    name = 'Mypackage',
    version = '0.1',
    pakackges = find_packages(exclude =['tests*']),
    license ='MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = "https//github.com/IMMA-M/Mypackge",
    author = "Imma",
    author_email = "Imma.gmail.com"
)