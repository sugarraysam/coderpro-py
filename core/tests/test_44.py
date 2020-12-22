from core.src.cp44_max_subarray import SubArray


def test_44_max_subarray():
    cases = [
        {"in": [], "want": 0},
        {"in": [-1, -2, -3], "want": -1},
        {"in": [1, 2, 3], "want": 6},
        {"in": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "want": 6},
    ]
    for c in cases:
        assert SubArray(c["in"]).naive() == c["want"]
        assert SubArray(c["in"]).linear() == c["want"]
