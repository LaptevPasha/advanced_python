"""Homework2: Pavel Laptev."""
import gc


def g():
    """
    Create a list of tuple referrers to marker.

    Return generator object.
    """
    marker = object()
    yield marker
    [tup] = [x for x in gc.get_referrers(marker) if type(x) is tuple]
    print(tup[1])


tuple(g())
