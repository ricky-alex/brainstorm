"""Device abstraction -- unified interface for compute hardware."""

from __future__ import annotations
from typing import Optional, List
from enum import Enum


class DeviceType(Enum):
    CPU = "cpu"
    CUDA = "cuda"
    ROCM = "rocm"


class Device:
    """Unified compute device abstraction.

    Provides a single interface regardless of whether you're running
    on CPU, NVIDIA CUDA, or AMD ROCm. This is the cornerstone of
    Brainstorm's hardware portability.
    """

    def __init__(self, device_type: DeviceType, index: int = 0):
        self.type = device_type
        self.index = index
        self.name = f"{device_type.value}:{index}"
        self._initialized = False

    def initialize(self) -> None:
        """Initialize the device and verify availability."""
        if self.type == DeviceType.ROCM:
            self._init_rocm()
        elif self.type == DeviceType.CUDA:
            self._init_cuda()
        self._initialized = True

    def _init_rocm(self) -> None:
        """Initialize AMD ROCm runtime."""
        try:
            import torch
            if torch.cuda.is_available() and torch.version.hip:
                torch.cuda.set_device(self.index)
        except ImportError:
            pass

    def _init_cuda(self) -> None:
        """Initialize NVIDIA CUDA runtime."""
        try:
            import torch
            if torch.cuda.is_available():
                torch.cuda.set_device(self.index)
        except ImportError:
            pass

    def __repr__(self) -> str:
        return f"Device({self.name})"


def get_device(name: Optional[str] = None) -> Device:
    """Get a device by name. Defaults to best available."""
    if name is None:
        try:
            import torch
            if torch.cuda.is_available():
                if hasattr(torch.version, "hip") and torch.version.hip:
                    return Device(DeviceType.ROCM, 0)
                return Device(DeviceType.CUDA, 0)
        except ImportError:
            pass
        return Device(DeviceType.CPU, 0)
    parts = name.split(":")
    dtype = DeviceType(parts[0])
    index = int(parts[1]) if len(parts) > 1 else 0
    return Device(dtype, index)


def list_devices() -> List[Device]:
    """List all available compute devices."""
    devices = [Device(DeviceType.CPU, 0)]
    try:
        import torch
        if torch.cuda.is_available():
            for i in range(torch.cuda.device_count()):
                if hasattr(torch.version, "hip") and torch.version.hip:
                    devices.append(Device(DeviceType.ROCM, i))
                else:
                    devices.append(Device(DeviceType.CUDA, i))
    except ImportError:
        pass
    return devices
