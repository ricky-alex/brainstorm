"""Training loop with progress tracking and checkpointing."""

from __future__ import annotations
from typing import Any, Dict, Optional, Callable, List
from brainstorm.utils.logging import get_logger
from brainstorm.utils.profiler import Profiler

logger = get_logger("trainer")


class Trainer:
    """High-level training orchestrator.

    Manages the training loop, validation, checkpointing, and
    metrics logging. Designed for clarity and extensibility.
    """

    def __init__(self, model: Any, optimizer: Any, loss_fn: Callable,
                 device: Optional[Any] = None):
        self.model = model
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.device = device
        self.profiler = Profiler()
        self.history: Dict[str, list] = {"train_loss": [], "val_loss": []}

    def fit(self, train_loader: Any, val_loader: Optional[Any] = None,
            epochs: int = 10, callbacks: Optional[list] = None) -> Dict[str, list]:
        """Run the training loop."""
        for epoch in range(epochs):
            with self.profiler.track(f"epoch_{epoch}"):
                train_loss = self._train_epoch(train_loader)
                self.history["train_loss"].append(train_loss)
                if val_loader:
                    val_loss = self._validate(val_loader)
                    self.history["val_loss"].append(val_loss)
                    logger.info(f"Epoch {epoch+1}/{epochs} -- train_loss: {train_loss:.4f}, val_loss: {val_loss:.4f}")
                else:
                    logger.info(f"Epoch {epoch+1}/{epochs} -- train_loss: {train_loss:.4f}")
        return self.history

    def _train_epoch(self, loader: Any) -> float:
        total_loss = 0.0
        for batch in loader:
            loss = 0.0  # placeholder
            total_loss += loss
        return total_loss / max(len(loader), 1)

    def _validate(self, loader: Any) -> float:
        total_loss = 0.0
        for batch in loader:
            total_loss += 0.0
        return total_loss / max(len(loader), 1)
