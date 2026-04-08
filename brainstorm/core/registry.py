"""Component registry for plugin discovery."""

from __future__ import annotations
from typing import Dict, Type


class Registry:
    """Global component registry.

    Enables plugin-style registration of modules, transforms,
    and other components without circular imports.
    """

    _components: Dict[str, Dict[str, Type]] = {
        "modules": {}, "transforms": {}, "optimizers": {}, "callbacks": {},
    }

    @classmethod
    def register(cls, category: str, name: str, component: Type) -> None:
        if category not in cls._components:
            cls._components[category] = {}
        cls._components[category][name] = component

    @classmethod
    def get(cls, category: str, name: str) -> Type:
        return cls._components.get(category, {}).get(name)

    @classmethod
    def list(cls, category: str) -> list:
        return list(cls._components.get(category, {}).keys())
