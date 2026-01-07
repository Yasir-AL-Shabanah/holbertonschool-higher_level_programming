#!/usr/bin/env python3
"""Task 03: CountedIterator - track iteration count."""


class CountedIterator:
    """Iterator wrapper that counts yielded items."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self._count += 1
        return item

    def get_count(self):
        return self._count
