from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import filterpy

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='censio-filterpy',
    version="1.0.UNKNOWN",
    description='Kalman filtering and optimal estimation library',
    long_description=long_description,
    url='https://github.com/rlabbe/filterpy',
    author='Roger Labbe',
    author_email='rlabbejr@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=['contrib']),
    install_requires=[
        # Feel free to raise these version numbers any time,
        # I just wanted to pin them in order to not break anything upstream
        # when a new numpy/scipy version is released
        'numpy<=1.18.1',
        'scipy<=1.4.1'
    ],
    tests_require = [
        'pytest'
    ],
    package_data={
        'filterpy': ['README.rst', 'changelog.txt', 'LICENSE.txt'],
    },
)
