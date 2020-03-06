import random

from src.binarysearch import BinarySearch


def test_binary_search():
    cases = [
        {"in": [1, 1, 3, 4, 5], "target": 1, "want": (True, 0)},
        {"in": [], "target": 1, "want": (False, -1)},
        {"in": list(range(1000)), "target": 1000, "want": (False, -1)},
    ]
    for c in cases:
        bs = BinarySearch(c["in"])
        assert bs.recursive(c["target"]) == c["want"]
        assert bs.iterative(c["target"]) == c["want"]
