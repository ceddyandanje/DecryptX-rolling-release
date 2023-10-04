import setuptools
from setuptools import setup, find_packages

setup(
    name='DecryptX',
    version='1.0.0',
    description='Password and hash cracker',
    author='Cedrick Andanje',
    author_email='rootaccessdenied4312@gmail.com',
    packages=find_packages(),
    install_requires=[
        'collections', 'hashlib', 'argparse', 'io', 'os', 'colorama', 'time'
    ],
)
