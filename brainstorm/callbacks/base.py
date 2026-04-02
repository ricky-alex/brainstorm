"""Callback system for training hooks."""

from __future__ import annotations
from typing import Any, Dict, List, Optional


class Callback:
    """Base callback for training events."""

    def on_epoch_start(self, epoch: int, logs: Optional[Dict] = None) -> None:
        pass

    def on_epoch_end(self, epoch: int, logs: Optional[Dict] = None) -> None:
        pass

    def on_batch_start(self, batch: int, logs: Optional[Dict] = None) -> None:
        pass

    def on_batch_end(self, batch: int, logs: Optional[Dict] = None) -> None:
        pass

    def on_train_start(self, logs: Optional[Dict] = None) -> None:
        pass

    def on_train_end(self, logs: Optional[Dict] = None) -> None:
        pass


class CallbackList:
    """Manage multiple callbacks."""

    def __init__(self, callbacks: Optional[List[Callback]] = None):
        self.callbacks = callbacks or []

    def add(self, callback: Callback) -> None:
        self.callbacks.append(callback)

    def on_epoch_end(self, epoch: int, logs: Optional[Dict] = None) -> None:
        for cb in self.callbacks:
            cb.on_epoch_end(epoch, logs)
