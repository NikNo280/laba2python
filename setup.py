from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="laba2",
    version="0.1",
    author="Nikita Sidorenko",
    author_email="nikitastar280@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Windows",
    ],
    python_requires='>=3.8',
)