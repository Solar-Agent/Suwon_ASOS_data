# setup.py

from setuptools import setup, find_packages

setup(
    name="Suwon_ASOS_data",
    version="0.1.0",
    author="Sooyoung",
    author_email="sooyoung.wind@gmail.com",
    description="Suwon ASOS data",
    license="MIT",
    packages=find_packages(),
    install_requires=["pandas"],
    python_requires=">=3.10",
)