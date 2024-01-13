import click
from pathlib import Path #py -m pip install pathlib.path

@click.command()
@click.argument('path') #add a new cl arg path to the ls custom command

def cli(path):
    target_dir = Path(path)

    if not target_dir.exists():
        click.echo('The target directory does not exist')
        raise SystemExit(1)
    
    for entry in target_dir.iterdir():
        click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

    click.echo()

if __name__ == "__main__":
    cli()

#Run it
    #python ls.py path
