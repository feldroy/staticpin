import pathlib

import httpx


def fetch_by_version(name: str, version: str, static_dir: pathlib.Path):
    # Using cdnjs API
    url = f"https://api.cdnjs.com/libraries/{name}/{version}"
    meta = httpx.get(url).json()
    for file in meta["files"]:
        if file.endswith(".min.js") or file.endswith(".min.css"):
            content = httpx.get(f"https://cdnjs.cloudflare.com/ajax/libs/{name}/{version}/{file}")
            dest = static_dir / name / file
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content.content)
            print(f"✓ {dest}")
