# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DCTDenoise',
    version='0.1.0',
    description='Simple DCT denoiser',
    long_description=readme,
    author='DorianMood',
    author_email='dorianmood@163.com',
    url='https://github.com/nekithockey75/DCTDenoise',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
