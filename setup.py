from setuptools import setup

setup(
	name='pystagram',
	version='1.0',
	description='API for downloading Instagram videos',
	author='Justin Chen',
	url='https://github.com/ch3njust1n/pystagram',
	py_modules=['pystagram'],
	install_requires=[
		'requests',
		'urllib'
	]
)