from src.permutations import sol


def test_perm():
    cases = [
        {
            "in": [1, 2, 3],
            "want": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
        },
        {"in": [1, 5], "want": [[1, 5], [5, 1]]},
    ]
    for c in cases:
        assert sol(c["in"]) == c["want"]
