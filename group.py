import click 
import os
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

@click.group()
def main():
    pass

#R like manner attempts using python
@main.command()
@click.option(
    "-sd",
    "--setwd",
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

def setwd(getwd, setwd, dpath):
    if not getwd and not setwd and dpath is None:
        click.echo(f"Choose one option between getwd or setwd. Terminal exiting")
        raise SystemExit(1)
        #exit(0)

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


@main.command()
@click.argument("path")
def ls(path):
    target_dir = Path(path)
    if not target_dir.exists():
        click.echo("The target directory doesn't exist")
        raise SystemExit(1)

    for entry in target_dir.iterdir():
        click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

    click.echo()

if __name__ == "__main__":
    main()
