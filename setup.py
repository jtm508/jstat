from setuptools import setup
import os

setup(
	name="J Stat",
	version = 0.1,
	url="https://github.com/jtm508/jstat/build/html/index.html",
	description = "Statistics Package",
	author = "Justin Max",
	author_email = "jtm508@gmail.com",
	packages=["jstat"],
	package_dir = {
		"jstat":"jstat"
		},
	install_requires=[
		"numpy>=1.10.4"
		]
)