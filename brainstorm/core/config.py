"""Configuration management for Brainstorm."""

from __future__ import annotations
from typing import Any, Dict, Optional
import json
import os


class Config:
    """Hierarchical configuration with file persistence.

    Supports JSON and environment variable overrides.
    """

    def __init__(self, defaults: Optional[Dict] = None):
        self._data: Dict[str, Any] = defaults or {}
        self._overrides: Dict[str, Any] = {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value with dot-notation support."""
        keys = key.split(".")
        value = self._overrides.get(key) or self._data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    def set(self, key: str, value: Any) -> None:
        """Set an override value."""
        self._overrides[key] = value

    def load(self, path: str) -> None:
        """Load configuration from JSON file."""
        with open(path) as f:
            self._data.update(json.load(f))

    def load_env(self, prefix: str = "BRAINSTORM_") -> None:
        """Load overrides from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower().replace("__", ".")
                self._overrides[config_key] = value

    def to_dict(self) -> Dict[str, Any]:
        """Export merged configuration."""
        result = dict(self._data)
        result.update(self._overrides)
        return result
