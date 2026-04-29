# Getting Started with Brainstorm

## Installation

```bash
pip install brainstorm-ai
pip install brainstorm-ai[rocm]  # AMD GPU support
```

## Your First Project

```python
from brainstorm import Engine, Pipeline, Module

class Classifier(Module):
    def __init__(self):
        super().__init__("classifier")
    def forward(self, x):
        return {"class": "positive", "confidence": 0.95}

pipeline = Pipeline("sentiment")
pipeline.add(Classifier())

engine = Engine()
result = engine.execute(pipeline, "Brainstorm is amazing!")
print(result)
```
