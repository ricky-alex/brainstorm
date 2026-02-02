"""Pipeline -- composable data processing chains."""

from __future__ import annotations
from typing import Any, List, Optional
from brainstorm.core.module import Module


class Pipeline(Module):
    """A sequential chain of modules that process data end-to-end.

    Pipelines are the primary way to compose Brainstorm modules.
    Data flows through each stage in order.

    Example:
        >>> pipeline = Pipeline("my-pipeline")
        >>> pipeline.add(Tokenizer())
        >>> pipeline.add(Encoder())
        >>> pipeline.add(Classifier())
        >>> result = pipeline.run(input_data)
    """

    def __init__(self, name: str, stages: Optional[List[Module]] = None):
        super().__init__(name)
        self.stages: List[Module] = stages or []

    def add(self, module: Module) -> "Pipeline":
        """Add a processing stage to the pipeline."""
        self.stages.append(module)
        self.add_child(module)
        return self

    def forward(self, data: Any, **kwargs: Any) -> Any:
        """Execute all stages sequentially."""
        result = data
        for stage in self.stages:
            result = stage.forward(result, **kwargs)
        return result

    def run(self, data: Any, device: Any = None) -> Any:
        """Run the pipeline with optional device placement."""
        return self.forward(data)

    def __len__(self) -> int:
        return len(self.stages)

    def __repr__(self) -> str:
        stages = " -> ".join(s.name for s in self.stages)
        return f"Pipeline('{self.name}': {stages})"
