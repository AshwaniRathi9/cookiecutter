#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Ashwani Rathi",
    author_email='rathiashwani8@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is the basic end to end ml project tutorial",
    entry_points={
        'console_scripts': [
            'mlproject=mlproject.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mlproject',
    name='mlproject',
    packages=find_packages(include=['mlproject', 'mlproject.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AshwaniRathi9/mlproject',
    version='0.0.1',
    zip_safe=False,
)
