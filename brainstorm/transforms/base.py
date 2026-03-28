"""Base transform classes."""

from __future__ import annotations
from typing import Any, List, Callable
from abc import ABC, abstractmethod


class Transform(ABC):
    """Base transform class."""

    @abstractmethod
    def __call__(self, data: Any) -> Any:
        ...


class Compose(Transform):
    """Chain multiple transforms."""

    def __init__(self, transforms: List[Transform]):
        self.transforms = transforms

    def __call__(self, data: Any) -> Any:
        for t in self.transforms:
            data = t(data)
        return data


class Lambda(Transform):
    """Wrap a function as a transform."""

    def __init__(self, fn: Callable):
        self.fn = fn

    def __call__(self, data: Any) -> Any:
        return self.fn(data)
