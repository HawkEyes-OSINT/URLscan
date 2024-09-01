import os
from setuptools import setup, find_packages

# Read the contents of the README.md file
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='urlscan-lib',
    version='0.1.0',
    description='A Python library for interacting with the URLScan.io API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='HawkEyes',
    url='https://github.com/HawkEyes-OSINT/URLscan',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
