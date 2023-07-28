from typing import Dict, List

from setuptools import find_packages, setup

_version = "0.0.0a0"

_deps = [
    "black==22.12.0",
    "flake8==3.9.2",
    "isort==5.8.0",
    "mypy",
]


def _setup_install_requires() -> Dict:
    return _deps


def _setup_packages() -> List:
    return find_packages(
        "src",
    )


def _setup_package_dir() -> Dict:
    return {"": "src"}


setup(
    name="Coding Problems",
    version=_version,
    description=("CLI for simple games"),
    keywords=(),
    install_requires=_setup_install_requires(),
    package_dir=_setup_package_dir(),
    packages=_setup_packages(),
)
