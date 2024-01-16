#!/usr/bin/env python3 #called the shebang for Ubuntu
import click 
import os
#import warnings
from pathlib import Path
#from common.globalconfig import GlobalConfig

@click.group()
def main():
    pass

@click.command()
@click.argument('setpath',
                type=click.Path(
                    exists=False,
                    file_okay=False,
                    readable=True,
                    path_type=Path),
                    )

def setwd(setpath):
    if not Path(setpath).exists():
        
        click.echo(os.makedirs(setpath))
        
    else:
        click.echo(os.chdir(setpath))

@click.command()
def getwd():
        click.echo(print(os.getcwd()))
        
#register commands-DOES NOT SEEM TO WORK
main.add_command(setwd)
main.add_command(getwd)
#global_config = GlobalConfig()-Here for use when using some global configs.

#warnings.warn("R-like commands", category=Warning, filename=None, lineno=1)
#Unable to implement warnings yet since I have not been able to decipher the filename param.

#Note
#This approach does not work not just because registering commands fails but because these commands need to be grouped when using
#multiple commands. This is where I started.
#Just to remember this:
# SET var = %cd%
# echo %var%
