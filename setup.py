from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jsfix/__init__.py
from jsfix import __version__ as version

setup(
	name="jsfix",
	version=version,
	description="App for fixtures transport",
	author="JS",
	author_email="jirisir@seznam.cz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
