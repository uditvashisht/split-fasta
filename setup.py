import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="split-fasta",
    version="1.0.0",
    description="A Command Line tool for splitting Fasta file with multiple sequences into individual Fasta files.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/uditvashisht/split-fasta",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["splitfasta"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "splitfasta=splitfasta.__main__:main",
        ]
    },
)
