"""Tests for `staticpin` package."""

import staticpin
from staticpin.utils import fetch_latest_version


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
