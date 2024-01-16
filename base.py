import click 
import os
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

@click.group()
def main():
    pass

#R like manner attempts using python
@click.command()
@click.option(
    "-sd",
    "--setwd", #@click.option("--setwd/--getwd", default=False) = binary options

    is_flag=True,
    default=False,
    help="Set the working directory to an existing directory of choice",
)
@click.option(
    "-gd",
    "--getwd",
    is_flag=True,
    default=False,
    help="Get the current working directory",
)
@click.argument('dpath',
                type=click.Path(
                    exists=False,
                    file_okay=False,
                    readable=True,
                    path_type=Path),
                    )

def directory_flow(getwd, setwd, dpath):
    if not getwd and not setwd and dpath is None:
        click.echo(f"Choose one option between getwd or setwd. Terminal exiting")
        exit(0)

    elif getwd:
        click.echo(f"The current working directory is , {os.getcwd()}")

    elif setwd:
        if not Path(dpath).exists():
            try:
                new_path = os.makedirs(dpath)
                click.echo(os.chdir( str(new_path)) )
            except Exception:
                f"Unable to create a new directory"
        else:
            click.echo(os.chdir(str(dpath)))


if __name__ == "__main__":
    directory_flow()
#main.add_command(directory_flow)

#From my observations with click:
    #1. I can define my argument as in this case with path and define my command (or function for the command) and in this case I need to define
    #not use the command (function name) but simply use my options and arguments.

    #2. Conversely, not using arguments means the command (function) must be called alongside the options defined.