import pathlib

import httpx
from rich.progress import track
from rich.console import Console

console = Console()

def fetch_latest_version(name: str) -> str:
    """Fetch the latest version number of a library from cdnjs."""
    url = f"https://api.cdnjs.com/libraries/{name}?fields=version"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()["version"]


def fetch_by_version(name: str, version: str, static_dir: pathlib.Path):
    # Using cdnjs API
    url = f"https://api.cdnjs.com/libraries/{name}/{version}"
    meta = httpx.get(url).json()
    console.print(f"Pinning {name} @ {version} @ {static_dir}")
    for file in track(meta["files"], description="Pinning..."):
        if file.endswith(".min.js") or file.endswith(".min.css"):
            content = httpx.get(f"https://cdnjs.cloudflare.com/ajax/libs/{name}/{version}/{file}")
            dest = static_dir / name / file
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content.content)
            console.print(f"✓ {dest}")
