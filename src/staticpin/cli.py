"""Console script for staticpin."""

from pathlib import Path

import typer
from rich.console import Console

from . import utils

app = typer.Typer()
console = Console()


@app.command()
def add(
    name: str,
    version: str = typer.Argument("", help="Version to install. If not specified, the latest version will be used."),
    static_dir: Path = Path("static"),
):
    """Add a dependency."""
    if version.strip() == "":
        version = utils.fetch_latest_version(name)
    console.print(f"Adding {name} @ {version}")


@app.command()
def upgrade(
    name: str,
    version: str = typer.Argument("", help="Version to upgrade to. If not specified, the latest version will be used."),
    static_dir: Path = Path("static"),
):
    """Update a dependency."""
    if version.strip() == "":
        version = utils.fetch_latest_version(name)
    console.print(f"Upgrading {name} to {version}")


@app.command()
def remove(name: str, static_dir: Path = Path("static")):
    """Remove a dependency."""
    console.print(f"Removing {name}")


if __name__ == "__main__":
    app()
