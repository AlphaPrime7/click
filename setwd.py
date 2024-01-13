#!/usr/bin/env python3 #called the shebang
import click 
import os
import warnings
from pathlib import Path
from warnings import warn

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
        #warnings.warn("In R manner, cli will attempt to make a directory for you but fail if spellings are wrong", category=Warning, filename=None, lineno=1)
        click.echo(os.makedirs(setpath))
        
    else:
        click.echo(os.chdir(setpath))
        
if __name__ == "__main__":
    setwd()








