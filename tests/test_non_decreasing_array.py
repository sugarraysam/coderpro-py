from src.non_decreasing_array import Solution


def test_non_decreasing():
    cases = [
        {"in": [], "want": True},
        {"in": [4], "want": True},
        {"in": [4, 2, 3], "want": True},
        {"in": [2, 3, 0], "want": True},
        {"in": [1, 2, 3, 4, 5, 4, 5, 7], "want": True},
        {"in": [1, 2, 3, 4, 5, 4, 3, 7], "want": False},
        {"in": [1, 2, 3, 2, 5, 6, 4, 7], "want": False},
    ]
    for c in cases:
        assert Solution(c["in"]).solution() == c["want"]
