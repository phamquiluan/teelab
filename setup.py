import os
from setuptools import find_packages, setup

version = "0.0.1"

setup(
    name="teelab",
    description="",
    author="Luan Pham",
    author_email="phamquiluan@gmail.com",
    version=version,
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=["opencv-python", "numpy"],
    extras_require={
        "dev": ["ipython", "tqdm", "pre-commit", "pytest"]
    }
)

