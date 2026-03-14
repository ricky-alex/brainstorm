"""HTTP model serving with FastAPI integration."""

from __future__ import annotations
from typing import Any, Optional, Dict
from brainstorm.utils.logging import get_logger

logger = get_logger("server")


class ModelServer:
    """Lightweight model serving wrapper.

    Wraps a Brainstorm model and exposes it via HTTP for
    production inference workloads.
    """

    def __init__(self, model: Any, host: str = "0.0.0.0", port: int = 8080):
        self.model = model
        self.host = host
        self.port = port
        self._request_count = 0

    def predict(self, data: Any) -> Any:
        """Run inference on input data."""
        self._request_count += 1
        return self.model.forward(data) if hasattr(self.model, "forward") else data

    def health(self) -> Dict[str, Any]:
        """Health check endpoint."""
        return {
            "status": "healthy",
            "model": getattr(self.model, "name", "unknown"),
            "requests_served": self._request_count,
        }

    def start(self) -> None:
        """Start the HTTP server."""
        try:
            from fastapi import FastAPI
            import uvicorn
            app = FastAPI()

            @app.post("/predict")
            async def predict_endpoint(data: dict):
                return {"result": self.predict(data)}

            @app.get("/health")
            async def health_endpoint():
                return self.health()

            logger.info(f"Starting server on {self.host}:{self.port}")
            uvicorn.run(app, host=self.host, port=self.port)
        except ImportError:
            logger.warning("FastAPI not installed. Install with: pip install fastapi uvicorn")
