from src.uniq_path import Solution


def test_uniq_path():
    cases = [
        {"m": 0, "n": 0, "want": 0},
        {"m": 1, "n": 0, "want": 0},
        {"m": 0, "n": 1, "want": 0},
        {"m": 1, "n": 1, "want": 0},
        {"m": 3, "n": 2, "want": 3},
        {"m": 7, "n": 3, "want": 28},
    ]
    for c in cases:
        sol = Solution(c["m"], c["n"])
        assert sol.backtrack() == c["want"]
        assert sol.singlerow() == c["want"]
        assert sol.combinatory() == c["want"]
