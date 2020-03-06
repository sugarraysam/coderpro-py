from src.product_except_self import Solution


def test_sol():
    cases = [
        {"in": [1, 2, 3, 4], "want": [24, 12, 8, 6]},
        {"in": [], "want": []},
        {"in": [3, 3, 3], "want": [9, 9, 9]},
        {"in": [2], "want": [0]},
    ]
    for c in cases:
        sol = Solution(c["in"])
        assert sol.with_div() == c["want"]
        assert sol.without_div() == c["want"]
