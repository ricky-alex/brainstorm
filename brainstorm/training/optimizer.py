"""Optimization algorithms."""

from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod
import math


class Optimizer(ABC):
    """Base optimizer class."""

    def __init__(self, params: List = None, lr: float = 1e-3):
        self.params = params or []
        self.lr = lr

    @abstractmethod
    def step(self) -> None:
        ...

    def zero_grad(self) -> None:
        for p in self.params:
            if hasattr(p, "grad"):
                p.grad = None


class SGD(Optimizer):
    """Stochastic Gradient Descent with optional momentum."""

    def __init__(self, params=None, lr=1e-3, momentum=0.0):
        super().__init__(params, lr)
        self.momentum = momentum
        self._velocity = [0.0] * len(self.params)

    def step(self) -> None:
        for i, p in enumerate(self.params):
            if hasattr(p, "grad") and p.grad is not None:
                self._velocity[i] = self.momentum * self._velocity[i] - self.lr * p.grad
                p.data += self._velocity[i]


class Adam(Optimizer):
    """Adam optimizer with bias correction."""

    def __init__(self, params=None, lr=1e-3, betas=(0.9, 0.999), eps=1e-8):
        super().__init__(params, lr)
        self.beta1, self.beta2 = betas
        self.eps = eps
        self._m = [0.0] * len(self.params)
        self._v = [0.0] * len(self.params)
        self._t = 0

    def step(self) -> None:
        self._t += 1
        for i, p in enumerate(self.params):
            if hasattr(p, "grad") and p.grad is not None:
                self._m[i] = self.beta1 * self._m[i] + (1 - self.beta1) * p.grad
                self._v[i] = self.beta2 * self._v[i] + (1 - self.beta2) * p.grad ** 2
                m_hat = self._m[i] / (1 - self.beta1 ** self._t)
                v_hat = self._v[i] / (1 - self.beta2 ** self._t)
                p.data -= self.lr * m_hat / (math.sqrt(v_hat) + self.eps)
