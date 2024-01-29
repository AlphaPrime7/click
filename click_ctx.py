#just decided to add these contexts snippets as I conclude notes but have had no real applications for this yet.
#Also gives me an idea of how we pass contexts when wrapping functions from outside sources into python.
#Also wondered how this is done in R as well and nice to see my nogging picked up on context pass through
import click

def callback(ctx, value):
    if not value:
        ctx.abort()

@click.command()
@click.option('--yes', is_flag=True, callback=callback,
              expose_value=False, prompt='Do you want to continue?')
def dropdb():
    pass