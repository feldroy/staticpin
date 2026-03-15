"""Console script for staticpin."""

from pathlib import Path

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def add(
    name: str,
    version: str = typer.Argument("", help="Version to install. If not specified, the latest version will be used."),
    static_dir: Path = Path("static"),
):
    """Add a dependency."""
    console.print(f"Adding {name}")


@app.command()
def upgrade(
    name: str,
    version: str = typer.Argument("", help="Version to upgrade to. If not specified, the latest version will be used."),
    static_dir: Path = Path("static"),
):
    """Update a dependency."""
    pass


@app.command()
def remove(name: str, static_dir: Path = Path("static")):
    """Remove a dependency."""
    pass


if __name__ == "__main__":
    app()
