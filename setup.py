# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="isPowerOf2",
    version="0.1.0",
    description="First Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Md Taslim Ansari",
    author_email="taslim.developer@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers & Students",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["isPowerOf2"],
    include_package_data=True
)
