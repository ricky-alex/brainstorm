"""The Brainstorm Engine -- orchestrates all computation."""

from __future__ import annotations
from typing import Any, Optional, Dict
from brainstorm.compute import Device, get_device


class Engine:
    """Central execution engine for Brainstorm.

    The Engine manages the lifecycle of computations, from data ingestion
    through model execution to output delivery. It abstracts hardware
    complexity and provides a unified interface for all operations.

    Example:
        >>> engine = Engine(device="cuda:0")
        >>> result = engine.execute(pipeline, data)
    """

    def __init__(self, device: Optional[str] = None, config: Optional[Dict] = None):
        self.device = get_device(device)
        self.config = config or {}
        self._pipelines: Dict[str, Any] = {}
        self._initialized = False

    def initialize(self) -> None:
        """Initialize the engine and verify hardware availability."""
        self.device.initialize()
        self._initialized = True

    def execute(self, pipeline: Any, data: Any) -> Any:
        """Execute a pipeline with given data."""
        if not self._initialized:
            self.initialize()
        return pipeline.run(data, device=self.device)

    def register_pipeline(self, name: str, pipeline: Any) -> None:
        """Register a named pipeline for reuse."""
        self._pipelines[name] = pipeline

    def __repr__(self) -> str:
        return f"Engine(device={self.device}, initialized={self._initialized})"
