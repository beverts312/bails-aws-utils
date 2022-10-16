from copyreg import constructor

from setuptools import find_packages, setup

__version__ = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bails-route53-utils",
    version=__version__,
    license="MIT",
    author="Bailey Everts",
    author_email="me@baileyeverts.net",
    description="For making route 53 easier",
    url="https://github.com/beverts312/bails-route53-utils",
    packages=find_packages(),
    install_requires=["boto3", "python-crontab", "requests"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=["bin/dynamic-dns"],
)
