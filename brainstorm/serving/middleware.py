"""Middleware for the model serving layer."""

from __future__ import annotations
from typing import Any, Callable
import time
from brainstorm.utils.logging import get_logger

logger = get_logger("middleware")


class RateLimiter:
    """Simple in-memory rate limiter."""

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window = window_seconds
        self._requests: list = []

    def allow(self) -> bool:
        now = time.time()
        self._requests = [t for t in self._requests if now - t < self.window]
        if len(self._requests) < self.max_requests:
            self._requests.append(now)
            return True
        return False


class RequestLogger:
    """Log all inference requests."""

    def __init__(self):
        self.request_count = 0
        self.total_latency = 0.0

    def wrap(self, fn: Callable) -> Callable:
        def wrapper(data: Any) -> Any:
            start = time.perf_counter()
            result = fn(data)
            latency = time.perf_counter() - start
            self.request_count += 1
            self.total_latency += latency
            logger.info(f"Request #{self.request_count} -- {latency*1000:.2f}ms")
            return result
        return wrapper
