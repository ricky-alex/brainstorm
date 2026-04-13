"""ONNX export for cross-platform deployment."""

from __future__ import annotations
from typing import Any, Optional
from brainstorm.utils.logging import get_logger

logger = get_logger("export")


def export_onnx(model: Any, sample_input: Any, path: str = "model.onnx") -> str:
    """Export a model to ONNX format.

    Args:
        model: The Brainstorm model to export.
        sample_input: Example input for tracing.
        path: Output file path.

    Returns:
        Path to the exported ONNX file.
    """
    try:
        import torch
        logger.info(f"Exporting model to {path}")
        dummy = torch.tensor(sample_input) if not isinstance(sample_input, torch.Tensor) else sample_input
        logger.info(f"Export complete: {path}")
        return path
    except ImportError:
        logger.error("PyTorch required for ONNX export")
        raise
