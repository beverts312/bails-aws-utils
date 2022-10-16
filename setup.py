from setuptools import find_packages, setup

__version__ = "0.2.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bails-aws-utils",
    version=__version__,
    license="MIT",
    author="Bailey Everts",
    author_email="me@baileyeverts.net",
    description="For making AWS easier",
    url="https://github.com/beverts312/bails-aws-utils",
    packages=find_packages(),
    install_requires=["boto3", "python-crontab", "requests"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=["bin/dynamic-dns", "bin/gmail-mx-create"],
)
