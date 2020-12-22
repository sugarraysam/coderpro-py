from core.src.quicksort import Quicksort


def test_quicksort():
    cases = [
        {"in": [9, 8, 7, 6], "want": [6, 7, 8, 9]},
        {"in": [], "want": []},
        {"in": [5], "want": [5]},
        {"in": [1, 9, 1, 9, 3, 3], "want": [1, 1, 3, 3, 9, 9]},
    ]

    for c in cases:
        q = Quicksort(c["in"])
        assert q.recursive_new() == c["want"]
