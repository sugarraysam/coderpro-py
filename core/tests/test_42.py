from core.src.cp42_min_subarray_len import SubArray


def test_42_subarray_len():
    cases = [
        {"nums": [], "s": 4, "want": 0},
        {"nums": [1, 2, 3], "s": 4, "want": 2},
        {"nums": [1, 2, 3], "s": 7, "want": 0},
        {"nums": [0, 0, 0, 0], "s": 4, "want": 0},
        {"nums": [1, 1, 2, 3], "s": 2, "want": 1},
        {"nums": [1, 1, 2, 3], "s": 7, "want": 4},
        {"nums": [1, 1, 2, 3], "s": 3, "want": 1},
    ]
    for c in cases:
        assert SubArray(c["nums"], c["s"]).naive() == c["want"]
        assert SubArray(c["nums"], c["s"]).pointers() == c["want"]
