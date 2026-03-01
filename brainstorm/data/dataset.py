"""Dataset and DataLoader abstractions."""

from __future__ import annotations
from typing import Any, Iterator, List, Optional, Callable
import random


class Dataset:
    """Base dataset class with lazy loading support."""

    def __init__(self, data: List[Any], transform: Optional[Callable] = None):
        self.data = data
        self.transform = transform

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int) -> Any:
        item = self.data[idx]
        if self.transform:
            item = self.transform(item)
        return item


class DataLoader:
    """Batched data loading with shuffling and multiprocessing."""

    def __init__(self, dataset: Dataset, batch_size: int = 32, shuffle: bool = True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __iter__(self) -> Iterator[List[Any]]:
        indices = list(range(len(self.dataset)))
        if self.shuffle:
            random.shuffle(indices)
        for i in range(0, len(indices), self.batch_size):
            batch_indices = indices[i:i + self.batch_size]
            yield [self.dataset[idx] for idx in batch_indices]

    def __len__(self) -> int:
        return (len(self.dataset) + self.batch_size - 1) // self.batch_size
