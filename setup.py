from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="edimageprocessing",
    version="0.0.1",
    author="Eduardo Santos",
    author_email="eduardocorral296@gmail.com",
    description="Data Analyst / Software Developer",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Edu2566/ED-image-Processing-Package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.12.2",
)
