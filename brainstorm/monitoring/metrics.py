"""Metrics collection and export."""

from __future__ import annotations
from typing import Dict, List, Any


class MetricsCollector:
    """Collect and export runtime metrics.

    Tracks inference latency, throughput, memory usage,
    and custom metrics for production monitoring.
    """

    def __init__(self):
        self._counters: Dict[str, int] = {}
        self._gauges: Dict[str, float] = {}
        self._histograms: Dict[str, List[float]] = {}

    def increment(self, name: str, value: int = 1) -> None:
        self._counters[name] = self._counters.get(name, 0) + value

    def gauge(self, name: str, value: float) -> None:
        self._gauges[name] = value

    def histogram(self, name: str, value: float) -> None:
        self._histograms.setdefault(name, []).append(value)

    def record_inference(self, latency_ms: float) -> None:
        self.increment("inference.count")
        self.histogram("inference.latency_ms", latency_ms)
        self.gauge("inference.last_latency_ms", latency_ms)

    def export(self) -> Dict[str, Any]:
        result = {"counters": dict(self._counters), "gauges": dict(self._gauges)}
        for name, values in self._histograms.items():
            result[f"histogram.{name}"] = {
                "count": len(values),
                "mean": sum(values) / len(values) if values else 0,
                "min": min(values) if values else 0,
                "max": max(values) if values else 0,
            }
        return result
