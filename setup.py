import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.rst").read_text()
desc = (
        "Materials Informatics Package "
        + "Stability of Elasticity Analysis"
    )

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="SeaMatPy",
    version="0.0.2",
    author="Stefanos Papanikolaou",
    author_email="stephanos.papanikolaou@gmail.com",
    description="A package for performing the Stability of Elasticity Analysis in Raw Images of Material Deformation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MaterialInformatics/SeaMatPy",
    packages=find_packages(),
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=requirements,
)
