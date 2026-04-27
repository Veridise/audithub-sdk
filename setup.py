from pathlib import Path
from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "audithub-sdk"
VERSION = "1.0.2"
PYTHON_REQUIRES = ">= 3.9"
DESCRIPTION = "Generated Python SDK for the AuditHub API."
REQUIRES = [
    "python-dateutil >= 2.8.2",
    "httpx >= 0.28.1",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]
README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author="Veridise",
    url="https://github.com/Veridise/audithub-sdk",
    keywords=["AuditHub", "OpenAPI", "SDK", "API client"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    long_description_content_type='text/markdown',
    long_description=README,
    package_data={"audithub_sdk": ["py.typed"]},
)
