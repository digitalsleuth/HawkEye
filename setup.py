#!/usr/bin/env python3
from setuptools import setup

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="HawkEye",
    version="1.0",
    author="Abdallah Elshinbary",
    url="https://github.com/N1ght-W0lf/HawkEye",
    description=("Malware dynamic instrumentation tool based on frida framework"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "psutil",
        "frida",
    ],
    packages=["hawkeye",
    ],
    entry_points={
        "console_scripts": [
            "hawkeye = hawkeye.HawkEye:main",
        [,
    },
)
