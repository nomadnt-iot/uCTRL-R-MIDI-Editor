# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='uCTRL-R Editor',
    version='0.8.0',
    description='uCTRL-R Editor for uCTRL-R MIDI',
    long_description=readme,
    author='Filippo Sallemi',
    author_email='fsallemi@nomadnt.com',
    url='https://github.com/nomadnt/uCTRL-Editor',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)