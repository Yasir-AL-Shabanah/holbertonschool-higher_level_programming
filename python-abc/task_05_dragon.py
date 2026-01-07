#!/usr/bin/env python3
"""Task 05: Dragon - mastering mixins."""


class SwimMixin:
    """Swim behavior mixin."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Fly behavior mixin."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon gains swim and fly via mixins."""

    def roar(self):
        print("The dragon roars!")
