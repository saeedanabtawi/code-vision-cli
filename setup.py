from setuptools import setup


import os

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


# This call to setup() does all the work
setup(
    name="code-vision-cli",
    version="0.1.0",
    description="Code Vision",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Saeed Anabtawi",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["core"],
    include_package_data=True,
    install_requires=["networkx", "matplotlib", "argparse","pycparser"]
)
