from setuptools import setup, find_packages
import os, re


def readme(file_name: str):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


PACK_DATA = {
    "NAME": "xTerm",
    "AUTHOR": "Mmdrza",
    "AUTHOR_EMAIL": "Pymmdrza@gmail.com",
    "DESCRIPTION": "Professional modding to the terminal and changing the font of string texts",
    "LONG_DESCRIPTION": readme("README.md"),
    "LICENSE": "MIT",
    "URL": "https://github.com/xTerm/xTerm",
    "PACK_ISSUES": "https://github.com/xTerm/xTerm/issues",
    "PACK_GITHUB": "https://github.com/xTerm/xTerm",
    "LONG_DESCRIPTION_CONTENT_TYPE": "text/markdown",
    "CLASSIFIERS": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    "PYTHON_REQUIRES": ">=3.7",
}

setup(
    name=PACK_DATA["NAME"],
    version="1.6.3",
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    author=PACK_DATA["AUTHOR"],
    author_email=PACK_DATA["AUTHOR_EMAIL"],
    description=PACK_DATA["DESCRIPTION"],
    long_description=PACK_DATA["LONG_DESCRIPTION"],
    long_description_content_type=PACK_DATA["LONG_DESCRIPTION_CONTENT_TYPE"],
    license=PACK_DATA["LICENSE"],
    url=PACK_DATA["URL"],
    classifiers=PACK_DATA["CLASSIFIERS"],
    python_requires=PACK_DATA["PYTHON_REQUIRES"],
    include_package_data=True

)
