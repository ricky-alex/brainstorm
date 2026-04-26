"""Test helper functions."""

from typing import Any


def assert_close(actual: Any, expected: Any, atol: float = 1e-6, msg: str = "") -> None:
    """Assert two values are close."""
    if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        diff = abs(actual - expected)
        assert diff < atol, f"Not close: {actual} vs {expected} (diff={diff}). {msg}"
    else:
        assert actual == expected, f"{actual} != {expected}. {msg}"
