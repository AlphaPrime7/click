#This click project came as a result of not being able to understand using setuptools, maybe because i was unfamiliar with cmd.
#Upon getting closer to cmd by using this dedicated project, finally the additional commands are showing up.
#Now just to code them properly in setup tools and decide my route for bridging normfluodbf to python.
import os
#import pathlib
import warnings
from setuptools import setup, find_packages, Command
from typing import Any, Dict, Iterator, List
from warnings import warn

_VERSION = "1.5.2"

REQUIRED_PACKAGES = [
    "numpy",
    "pandas",
]

class CustomCommandClass(Command):

    description = "User options mimicking R and additional commands by subclassing setuptools.Command"

    user_options: List[Any] = [
        ('setwd=', 'swd', 'set working directory'),
        ('getwd=', 'gwd', 'get working directory'),
    ]

    def initialize_options(nofun, **kwargs):
        nofun.setwd = None
        nofun.getwd = None
        nofun.target_dir = None
    
    def finalize_options(nofun):
        if nofun.setwd is None:
            warnings.warn("In R like manner, the user is advised to set a working directory")
        else:
            pass

    def run(nofun):
        def getwd():
            pass

        def setwd(arg, target_dir):
            pass
        try:
            print('current directory set to:')
            os.makedirs(nofun.setwd)
        except FileExistsError:
            pass
                    
#with open('README.md') as readme_file:
    #readme = readme_file.read()

setup(
    author="alphaprime7",
    author_email="awesome.tingwei@outlook.com",
    maintainer= 'Tingwei Adeck',
    maintainer_email= "awesome.tingwei@outlook.com",
    url='https://github.com/alphaprime7/normfluodbf',
    project_urls={
        "Bug Tracker": "https://github.com/alphaprime7/normfluodbf/issues",
    },
    #license="MIT license",
    license="Apache 2.0",
    description="Cleans and Normalizes liposome flux assay DBF and DAT files from the FLUOStar Microplate Reader.",
    #long_description=readme,
    long_description_content_type="text/markdown",
    platforms= ['Windows', 'Linux', 'MacOS'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Quantitative",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        'Intended Audience :: Developers',
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        #'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    #distclass=BinaryDistribution,
    cmdclass={
        'getwd': CustomCommandClass,
        'setwd': CustomCommandClass
    },
    include_package_data=True,
    #data_files=[('', data_files)],
    keywords='dat',
    name='normfluodbf',
    # package_dir={'': '.'},
    packages=find_packages(include=['core','sub',
                                    'core.*','sub.*']),
    install_requires=REQUIRED_PACKAGES, 
    test_suite='tests',
    #version='1.5.2',
    zip_safe=False,
)
