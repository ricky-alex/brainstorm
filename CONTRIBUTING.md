# Contributing to Brainstorm

## Development Setup

```bash
git clone https://github.com/ricky-alex/brainstorm.git
cd brainstorm
pip install -e ".[dev]"
pre-commit install
```

## Code Standards

- Type hints required on all public APIs
- Docstrings in Google style format
- 100% test coverage for core modules
- All GPU code must pass ROCm validation

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Write tests for your changes
4. Ensure all CI checks pass
5. Submit a PR with a clear description
