# AMD ROCm Integration Guide

## Why ROCm?

Brainstorm was built with AMD hardware as a first-class citizen. ROCm is AMD's open-source GPU computing platform.

### Open Source Foundation

Unlike proprietary alternatives, ROCm is fully open source:

- Full transparency -- inspect every line of the runtime
- Community contributions -- improvements from researchers worldwide
- No vendor lock-in -- your code runs on any ROCm-compatible hardware
- Long-term support -- open source outlives any single company's product cycle

### Performance Characteristics

AMD GPUs excel in workloads that benefit from:

- High memory bandwidth (HBM2/HBM3)
- Large memory capacity for big models
- Efficient parallel compute for matrix operations
- Competitive price-to-performance ratio

### Supported Hardware

| GPU Series | Architecture | VRAM | Status |
|-----------|-------------|------|--------|
| MI300X | CDNA 3 | 192GB HBM3 | Full Support |
| MI250X | CDNA 2 | 128GB HBM2e | Full Support |
| MI210 | CDNA 2 | 64GB HBM2e | Full Support |
| RX 7900 XTX | RDNA 3 | 24GB GDDR6 | Beta |

## Performance Tips

1. Use FP16 -- AMD GPUs have strong half-precision performance
2. Batch size tuning -- MI300X's 192GB allows very large batches
3. Memory management -- Use Brainstorm's MemoryManager for optimal allocation
4. Kernel fusion -- Enable fused operations for reduced memory bandwidth
