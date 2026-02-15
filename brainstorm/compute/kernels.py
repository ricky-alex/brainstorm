"""Compute kernels -- optimized operations for supported hardware."""

from __future__ import annotations
from typing import Any, Optional


class KernelRegistry:
    """Registry for hardware-specific compute kernels.

    Automatically selects the best kernel for the current hardware.
    Falls back to generic implementations when specialized kernels
    are unavailable.
    """

    _kernels: dict = {}

    @classmethod
    def register(cls, name: str, device_type: str, kernel_fn):
        """Register a kernel for a specific device type."""
        key = f"{name}.{device_type}"
        cls._kernels[key] = kernel_fn

    @classmethod
    def get(cls, name: str, device_type: str, fallback: str = "cpu"):
        """Get the best kernel for the given device."""
        key = f"{name}.{device_type}"
        if key in cls._kernels:
            return cls._kernels[key]
        return cls._kernels.get(f"{name}.{fallback}")


def vector_add(a, b, device=None):
    """Optimized vector addition with device dispatch."""
    if device and device.type.value == "rocm":
        return _rocm_vector_add(a, b)
    return _cpu_vector_add(a, b)


def _cpu_vector_add(a, b):
    """Generic CPU vector addition."""
    return [x + y for x, y in zip(a, b)]


def _rocm_vector_add(a, b):
    """ROCm-optimized vector addition."""
    import torch
    ta = torch.tensor(a, device="cuda")
    tb = torch.tensor(b, device="cuda")
    return (ta + tb).cpu().tolist()
