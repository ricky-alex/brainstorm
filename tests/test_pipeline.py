"""Tests for Pipeline."""

import pytest
from brainstorm.core.pipeline import Pipeline
from brainstorm.core.module import Module


class AddOne(Module):
    def __init__(self):
        super().__init__("add-one")
    def forward(self, x):
        return x + 1


class MultiplyByTwo(Module):
    def __init__(self):
        super().__init__("mul-two")
    def forward(self, x):
        return x * 2


def test_pipeline_sequential():
    p = Pipeline("test")
    p.add(AddOne())
    p.add(MultiplyByTwo())
    assert p.run(5) == 12


def test_pipeline_length():
    p = Pipeline("test")
    p.add(AddOne())
    p.add(MultiplyByTwo())
    assert len(p) == 2


def test_empty_pipeline():
    p = Pipeline("empty")
    assert p.run(42) == 42
