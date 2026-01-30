"""Base Module class -- the building block of all Brainstorm components."""

from __future__ import annotations
from typing import Any, Dict, Optional, List
from abc import ABC, abstractmethod


class Module(ABC):
    """Abstract base class for all Brainstorm modules.

    Every component in Brainstorm inherits from Module. This ensures
    consistent interfaces, serialization, and composability.

    Attributes:
        name: Unique identifier for this module.
        config: Configuration dictionary.
        trainable: Whether this module has trainable parameters.
    """

    def __init__(self, name: str, config: Optional[Dict] = None):
        self.name = name
        self.config = config or {}
        self.trainable = False
        self._parameters: Dict[str, Any] = {}
        self._children: List[Module] = []

    @abstractmethod
    def forward(self, *args: Any, **kwargs: Any) -> Any:
        """Forward pass -- must be implemented by subclasses."""
        ...

    def parameters(self) -> Dict[str, Any]:
        """Return all trainable parameters."""
        params = dict(self._parameters)
        for child in self._children:
            params.update(child.parameters())
        return params

    def add_child(self, module: Module) -> None:
        """Register a child module."""
        self._children.append(module)

    def state_dict(self) -> Dict[str, Any]:
        """Serialize module state."""
        return {"name": self.name, "config": self.config, "parameters": self._parameters}

    def load_state_dict(self, state: Dict[str, Any]) -> None:
        """Load module state from dictionary."""
        self._parameters = state.get("parameters", {})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
