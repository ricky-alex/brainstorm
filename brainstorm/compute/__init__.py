"""Compute layer -- hardware abstraction for GPU and CPU."""

from brainstorm.compute.device import Device, get_device, list_devices

__all__ = ["Device", "get_device", "list_devices"]
