#This click project came as a result of not being able to understand using setuptools, maybe because i was unfamiliar with cmd.
#Upon getting closer to cmd by using this dedicated project, finally the additional commands are showing up.
#Now just to code them properly in setup tools and decide my route for bridging normfluodbf to python.
import os
import pathlib
import click
import warnings
from setuptools import setup, find_packages, Command
from typing import Any, Dict, Iterator, List
from warnings import warn
from pathlib import Path

_VERSION = "1.5.2"

PROJECT_ROOT = os.path.dirname(__file__)

REQUIRED_PACKAGES = [
    "numpy",
    "pandas",
]

INSTALL_REQUIRES = [
     "numpy",
     "pandas",
]

#with open('README.md') as readme_file:
    #readme = readme_file.read()

with open(os.path.join(PROJECT_ROOT, "README.md")) as file_:
    long_description = file_.read()

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

        @click.group()
        def main():
            pass
        
        @main.command()
        def getwd(arg):
            os.getcwd()
            click.echo(f"The current working directory is , {os.getcwd()}")
        getwd()

        @main.command()
        @click.argument('target_dir',
                        type=click.Path(
                            exists=False,
                            file_okay=False,
                            readable=True,
                            path_type=Path),
                            )

        def setwd(arg,target_dir):
                 dpath = pathlib.PureWindowsPath(target_dir).as_posix()
                 if not Path(dpath).exists(): #pathlib.PureWindowsPath(dpath).as_posix()
                     try:
                         new_path = os.makedirs(dpath, exist_ok= True)
                         new_path
                         click.echo(os.chdir( str(new_path)) )
                     except FileNotFoundError:
                         click.echo(f"Directory: {dpath} does not exist but will be created if possible")
                         raise SystemExit(0)
                     except NotADirectoryError:
                         click.echo(f"{dpath} is not a directory but will be created if possible")
                         raise SystemExit(0)
                     except PermissionError:
                         click.echo(f"You do not have permissions to change to {dpath}")
                         raise SystemExit(0)
                     click.echo()

                 else:
                     try:
                         os.chdir(str(dpath))
                         click.echo(os.chdir(str(dpath)))
                     except FileNotFoundError:
                         click.echo(f"Directory: {dpath} does not exist")
                         raise SystemExit(0)
                     except NotADirectoryError:
                         click.echo(f"{dpath} is not a directory")
                         raise SystemExit(0)
                     except PermissionError:
                         click.echo(f"You do not have permissions to change to {dpath}")
                         raise SystemExit(0)
                     click.echo()
        setwd()


setup(
    author="alphaprime7",
    author_email="awesome.tingwei@outlook.com",
    maintainer= 'Tingwei Adeck',
    maintainer_email= "awesome.tingwei@outlook.com",
    url='https://github.com/alphaprime7/normfluodbf',
    project_urls={
        "Bug Tracker": "https://github.com/alphaprime7/normfluodbf/issues",
    },
    #version='1.5.2',
    license="MIT license",
    description="Cleans and Normalizes liposome flux assay DBF and DAT files from the FLUOStar Microplate Reader.",
    #long_description=readme,
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms= ['Windows', 'Linux', 'MacOS'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Environment :: Local Environment",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: STEM :: Quantitative",
        "Topic :: Bioinformatics",
        'Intended Audience :: Developers',
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    #distclass=BinaryDistribution,
    cmdclass={
        'getwd': CustomCommandClass,
        'setwd': CustomCommandClass
    },
    keywords=('dat','dbf','liposomes', 'research','bioinformatics', 'science', 'FLUOStar','BMG LABTECH'),
    name='normfluodbf',
    #packages=find_packages("src"), #src represents where source code is saved.
    #package_dir={'': 'src'}, #this performs link to the src dir.maybe better wording
    packages=find_packages(include=['core','sub',
                                    'core.*','sub.*']),
    #package_dir={'': '.'},

    #pkg data
    include_package_data=True,
    #data_files=[('', data_files)],

    #installation reqs
    install_requires=REQUIRED_PACKAGES, 

    #testing reqs
    #tests_require=INSTALL_REQUIRES + [
     #   "pytest",
      #  "pytest-asyncio",
    #], #OR
    test_suite='tests',

    zip_safe=False,
)
