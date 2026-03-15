"""Console script for staticpin."""

import typer
from rich.console import Console

from staticpin import utils

app = typer.Typer()
console = Console()



@app.command()
def add(dep: str, version: str = ''):
    """Add a dependency, if no version is specified pull the latest one"""
    pass

@app.command()
def upgrade(dep: str, version: str = ''):
    """Update a dependency, if no version is specified update to the latest one"""
    pass

@app.command()
def remove(dep: str):
    """Remove a dependency, if no version is specified pull the latest one"""
    pass


if __name__ == "__main__":
    app()
