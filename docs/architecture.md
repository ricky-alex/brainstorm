# Architecture Overview

Brainstorm follows a layered architecture designed for extensibility:

## Layer Stack

```
+-----------------------------------+
|         Application Layer         |  <- User code lives here
+-----------------------------------+
|         Pipeline Layer            |  <- Data flow orchestration
+-----------------------------------+
|         Compute Layer             |  <- GPU/CPU abstraction
+-----------------------------------+
|         Memory Layer              |  <- Tensor management
+-----------------------------------+
|         Hardware Layer            |  <- ROCm / HIP interface
+-----------------------------------+
```

## Design Principles

1. Zero-cost abstractions -- Overhead only where you need it
2. Hardware transparency -- Write once, run on any supported GPU
3. Composability -- Every module is a building block
4. Deterministic execution -- Reproducibility by default
