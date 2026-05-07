# Deployment Guide

## Docker

```dockerfile
FROM rocm/pytorch:latest
WORKDIR /app
COPY . .
RUN pip install -e .
EXPOSE 8080
CMD ["brainstorm", "serve", "--model", "production"]
```

## Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: brainstorm-inference
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: inference
        image: brainstorm:latest
        resources:
          limits:
            amd.com/gpu: 1
```

## Quantization

```python
from brainstorm.export import quantize
model = quantize(model, precision="int8")
```
