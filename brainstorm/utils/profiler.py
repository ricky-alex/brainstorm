"""Performance profiling utilities."""

from __future__ import annotations
import time
from typing import Dict, List
from contextlib import contextmanager


class Profiler:
    """Track execution time across code sections."""

    def __init__(self):
        self._timings: Dict[str, List[float]] = {}

    @contextmanager
    def track(self, name: str):
        """Context manager to time a code block."""
        start = time.perf_counter()
        yield
        elapsed = time.perf_counter() - start
        self._timings.setdefault(name, []).append(elapsed)

    def report(self) -> Dict[str, Dict[str, float]]:
        """Generate a summary report."""
        result = {}
        for name, times in self._timings.items():
            result[name] = {
                "count": len(times),
                "total": sum(times),
                "mean": sum(times) / len(times),
                "min": min(times),
                "max": max(times),
            }
        return result

    def print_report(self) -> None:
        """Print a formatted report."""
        report = self.report()
        for name, stats in report.items():
            print(
                f"  {name}: {stats['count']} calls, "
                f"mean={stats['mean']*1000:.2f}ms, "
                f"total={stats['total']*1000:.2f}ms"
            )
