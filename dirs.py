import click 
import os
import pathlib
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

@click.group()
def main():
    pass

@main.command()
def getwd():
    #pwd = os.getcwd()
    #pwd = os.path.realpath(__file__)
    click.echo(f"The current working directory is , {os.getcwd()}")

@main.command()
@click.argument('dpath',
                type=click.Path(
                    exists=False,
                    file_okay=False,
                    readable=True,
                    path_type=Path),
                    )
def setwd(dpath):
     dpath = pathlib.PureWindowsPath(dpath).as_posix()
     if not Path(dpath).exists(): #pathlib.PureWindowsPath(dpath).as_posix()
         try:
            new_path = os.makedirs(dpath, exist_ok= True)
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


@click.group()
def nomain():
    pass    

@nomain.command()
@click.argument("path")
def ls(path):
    target_dir = Path(path)
    if not target_dir.exists():
        click.echo("The target directory doesn't exist")
        raise SystemExit(1)

    for entry in target_dir.iterdir():
        click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

    click.echo()

dir = click.CommandCollection(sources=[main, nomain], help="These commands provide a way to manipulate directories using python")

if __name__ == "__main__":
    dir()