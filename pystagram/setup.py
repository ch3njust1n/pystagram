from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='pystagram',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="API for downloading Instagram videos",
    license="MIT",
    author="Justin Chen",
    author_email='ch3njus@gmail.com',
    url='https://github.com/ch3njust1n/pystagram',
    packages=['pystagram'],
    entry_points={
        'console_scripts': [
            'pystagram=pystagram.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='pystagram',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
