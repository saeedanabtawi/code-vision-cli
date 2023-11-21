from setuptools import setup, find_packages
import os
import code_vision_cli

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the README file

def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


install_requires = ["networkx", "matplotlib", "argparse", "pycparser","tqdm"]


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


# This call to setup() does all the work
setup(
    name="code-vision-cli",
    version=code_vision_cli.__version__,
    description="Code Vision",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="",
    author=code_vision_cli.__author__,
    license=code_vision_cli.__licence__,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=['code_vision_cli', 'code_vision_cli.*']),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'code-vision-cli = code_vision_cli.__main__:main',
        ],
    }, project_urls={
        'GitHub': 'https://github.com/saeedanabtawi/code-vision-cli'
    }
)
