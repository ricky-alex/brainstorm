"""Memory management for compute devices."""

from __future__ import annotations
from typing import Optional
import gc


class MemoryManager:
    """GPU memory allocation and tracking.

    Provides memory pooling, garbage collection, and OOM prevention
    for production workloads.
    """

    def __init__(self, device: "Device", pool_size: Optional[int] = None):
        self.device = device
        self.pool_size = pool_size
        self._allocated = 0
        self._peak = 0

    def allocate(self, size_bytes: int) -> "MemoryBlock":
        """Allocate memory on the device."""
        if self.pool_size and self._allocated + size_bytes > self.pool_size:
            self.gc()
            if self._allocated + size_bytes > self.pool_size:
                raise MemoryError(
                    f"OOM: requested {size_bytes} bytes, "
                    f"available {self.pool_size - self._allocated}"
                )
        self._allocated += size_bytes
        self._peak = max(self._peak, self._allocated)
        return MemoryBlock(size_bytes, self)

    def free(self, size_bytes: int) -> None:
        """Release allocated memory."""
        self._allocated = max(0, self._allocated - size_bytes)

    def gc(self) -> None:
        """Force garbage collection."""
        gc.collect()

    @property
    def stats(self) -> dict:
        return {
            "allocated": self._allocated,
            "peak": self._peak,
            "pool_size": self.pool_size,
        }


class MemoryBlock:
    """A tracked allocation on a device."""

    def __init__(self, size: int, manager: MemoryManager):
        self.size = size
        self.manager = manager

    def release(self) -> None:
        self.manager.free(self.size)

    def __del__(self):
        self.release()
