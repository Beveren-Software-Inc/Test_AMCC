from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amcc_app/__init__.py
from amcc_app import __version__ as version

setup(
	name="amcc_app",
	version=version,
	description="AMCC Custom Development",
	author="Shivansh",
	author_email="shivansh@beverensoftware.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
