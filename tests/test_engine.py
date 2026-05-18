"""Tests for the core Engine."""

import pytest
from brainstorm.core.engine import Engine
from brainstorm.core.pipeline import Pipeline
from brainstorm.core.module import Module


class DummyModule(Module):
    def __init__(self):
        super().__init__("dummy")
    def forward(self, x):
        return x * 2


def test_engine_creation():
    engine = Engine()
    assert not engine._initialized


def test_engine_execute():
    engine = Engine()
    pipeline = Pipeline("test")
    pipeline.add(DummyModule())
    result = engine.execute(pipeline, 5)
    assert result == 10
