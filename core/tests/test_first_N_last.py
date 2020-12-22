from core.src.first_N_last import solIterative, solNaive, solRecursive


def test_first_N_last():
    cases = [
        {"xint": [1, 3, 4, 4, 5, 9, 9, 10, 11], "target": 9, "want": (5, 6)},
        {"xint": [1, 4, 5, 9, 10, 11], "target": 4, "want": (1, 1)},
        {"xint": [1, 4, 5, 9, 10, 11], "target": 11, "want": (5, 5)},
    ]
    for c in cases:
        assert solNaive(c["xint"], c["target"]) == c["want"]
        assert solIterative(c["xint"], c["target"]) == c["want"]
        assert solRecursive(c["xint"], c["target"]) == c["want"]
