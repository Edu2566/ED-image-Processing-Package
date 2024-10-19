from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

requirements = [
    "certifi==2024.8.30",
    "charset-normalizer==3.4.0",
    "contourpy==1.3.0",
    "cycler==0.12.1",
    "docutils==0.21.2",
    "fonttools==4.54.1",
    "idna==3.10",
    "imageio==2.36.0",
    "importlib_metadata==8.5.0",
    "jaraco.classes==3.4.0",
    "jaraco.context==6.0.1",
    "jaraco.functools==4.1.0",
    "keyring==25.4.1",
    "kiwisolver==1.4.7",
    "lazy_loader==0.4",
    "markdown-it-py==3.0.0",
    "matplotlib==3.9.2",
    "mdurl==0.1.2",
    "more-itertools==10.5.0",
    "networkx==3.4.1",
    "nh3==0.2.18",
    "numpy==2.1.2",
    "packaging==24.1",
    "pillow==11.0.0",
    "pkginfo==1.10.0",
    "Pygments==2.18.0",
    "pyparsing==3.2.0",
    "python-dateutil==2.9.0.post0",
    "pywin32-ctypes==0.2.3",
    "readme_renderer==44.0",
    "requests==2.32.3",
    "requests-toolbelt==1.0.0",
    "rfc3986==2.0.0",
    "rich==13.9.2",
    "scikit-image==0.24.0",
    "scipy==1.14.1",
    "setuptools==75.2.0",
    "six==1.16.0",
    "tifffile==2024.9.20",
    "twine==5.1.1",
    "urllib3==2.2.3",
    "zipp==3.20.2"
]

setup(
    name="edimageprocessing",
    version="0.0.2",
    author="Eduardo Santos",
    author_email="eduardocorral296@gmail.com",
    description="Pypi Publishing Test With a Image Processing Image Process Pakage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Edu2566/ED-image-Processing-Package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.12.2",
)
