#!/usr/bin/python3
class MyList(list):
    """List subclass with sorted printer."""
    def print_sorted(self):
        print("{}".format(sorted(self)))
