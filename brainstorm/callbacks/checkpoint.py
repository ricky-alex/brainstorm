"""Checkpoint callback for model persistence."""

import json
import os
from typing import Optional, Dict
from brainstorm.callbacks.base import Callback
from brainstorm.utils.logging import get_logger

logger = get_logger("checkpoint")


class CheckpointCallback(Callback):
    """Save model checkpoints during training."""

    def __init__(self, directory: str = "checkpoints", save_best: bool = True):
        self.directory = directory
        self.save_best = save_best
        self.best_loss = float("inf")
        os.makedirs(directory, exist_ok=True)

    def on_epoch_end(self, epoch: int, logs: Optional[Dict] = None) -> None:
        logs = logs or {}
        loss = logs.get("val_loss", logs.get("train_loss", float("inf")))
        path = os.path.join(self.directory, f"epoch_{epoch}.json")
        with open(path, "w") as f:
            json.dump({"epoch": epoch, "loss": loss}, f)
        logger.info(f"Saved checkpoint: {path}")
        if self.save_best and loss < self.best_loss:
            self.best_loss = loss
            best_path = os.path.join(self.directory, "best.json")
            with open(best_path, "w") as f:
                json.dump({"epoch": epoch, "loss": loss}, f)
            logger.info(f"New best model: {loss:.4f}")
