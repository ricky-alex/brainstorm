"""Custom exceptions for Brainstorm."""


class BrainstormError(Exception):
    """Base exception for Brainstorm."""
    pass


class DeviceError(BrainstormError):
    """Hardware device errors."""
    pass


class PipelineError(BrainstormError):
    """Pipeline execution errors."""
    pass


class ConfigError(BrainstormError):
    """Configuration errors."""
    pass


class OOMError(BrainstormError):
    """Out of memory errors."""
    pass
