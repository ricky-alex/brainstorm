"""Brainstorm package setup."""

from setuptools import setup, find_packages

setup(
    name="brainstorm-ai",
    version="0.1.0",
    author="Ricky Alex",
    description="The Core AI Framework for Modern Intelligence",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["numpy>=1.24.0"],
    extras_require={
        "rocm": ["torch>=2.0"],
        "cuda": ["torch>=2.0"],
        "serving": ["fastapi>=0.100.0", "uvicorn>=0.23.0"],
        "dev": ["pytest>=7.0", "black", "ruff"],
    },
)
