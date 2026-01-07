#!/usr/bin/env python3
"""Task 02: Extending the Python list with notifications."""


class VerboseList(list):
    """List that prints notifications on mutations."""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
