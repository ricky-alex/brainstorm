# API Reference

## Core

### Engine(device=None, config=None)
Central execution engine.

- initialize() -- Init hardware
- execute(pipeline, data) -- Run a pipeline
- register_pipeline(name, pipeline) -- Register named pipeline

### Pipeline(name, stages=None)
Sequential processing chain.

- add(module) -- Add processing stage
- forward(data) -- Execute all stages
- run(data, device=None) -- Run with device

### Module(name, config=None)
Base class for all components.

- forward(*args, **kwargs) -- Abstract forward pass
- parameters() -- Get trainable parameters
- state_dict() -- Serialize state

## Training

### Trainer(model, optimizer, loss_fn)
- fit(train_loader, val_loader, epochs) -- Run training

### Adam / SGD
Optimization algorithms.

## Serving

### ModelServer(model, host, port)
- predict(data) -- Run inference
- health() -- Health check
- start() -- Start HTTP server
