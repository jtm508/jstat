from setuptools import setup
import os

setup(
	name="J Stat",
	version = 0.1,
	description = "Statistics Package",
	author = "Justin Max",
	author_email = "jtm508@gmail.com",
	package=["jstat"]
	package_dir = {
		"jstat":"jstat"
		},
	install_requires=[
		"numpy>=1.10.4"
		]
)