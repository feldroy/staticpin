"""Tests for `staticpin` package."""

import staticpin
from staticpin.utils import fetch_by_version, fetch_latest_version


def test_import():
    """Verify the package can be imported."""
    assert staticpin


def test_fetch_latest_version_htmx():
    """Verify we can fetch the latest version of htmx from cdnjs."""
    version = fetch_latest_version("htmx")
    # Should return a valid semver-like string
    parts = version.split(".")
    assert len(parts) >= 2, f"Expected a dotted version string, got {version!r}"
    # Major version should be a number
    assert parts[0].isdigit(), f"Major version not numeric: {version!r}"


def test_fetch_by_version_htmx(tmp_path):
    """Verify we can fetch a specific version of htmx and get the expected files."""
    fetch_by_version("htmx.org", "2.0.4", tmp_path)
    lib_dir = tmp_path / "htmx.org"
    assert lib_dir.exists(), "Library directory was not created"
    min_js = list(lib_dir.rglob("*.min.js"))
    assert min_js, "No .min.js files were downloaded"
    for f in min_js:
        assert f.stat().st_size > 0, f"Downloaded file is empty: {f}"
