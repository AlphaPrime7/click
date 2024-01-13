import click 
import os
import warnings
from pathlib import Path
from warnings import warn


@click.command()
@click.argument('setpath',
                type=click.Path(
                    exists=True,
                    file_okay=False,
                    readable=True,
                    path_type=Path),
                    )
@click.argument('makepath',
                type=click.Path(
                    exists=True,
                    file_okay=False,
                    readable=True,
                    path_type=Path),
                    )

def setwd(setpath = None):

    if setpath is None:
        if not setpath.exists():
            #click.echo("In R manner set a working directory")
            click.echo(warnings.warn("In R manner, the user is advised to set a working directory")) 
            raise SystemExit(1)
        else:
            click.echo(os.chdir(setpath))
    else:
        click.echo(os.chdir(setpath))

def makewd(makepath = None):

    if makepath is None:
        #another error handling tool-enter is considered click and then the message is echo
        click.echo(warnings.warn("In R manner, the user is advised to set a working directory")) 
        pass
    else:
        click.echo(os.makedirs(makepath))

if __name__ == "__main__":
    setwd()

if __name__ == "__main__":
    makewd()







