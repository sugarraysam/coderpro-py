from src.threesum import Solution, Triplet


def test_threesum():
    cases = [
        {"in": [], "want": []},
        {
            "in": [-1, 0, 1, 2, -1, 4],
            "want": [Triplet([-1, 0, 1]), Triplet([2, -1, -1])],
        },
    ]
    for c in cases:
        assert Solution(c["in"]).hashmap() == c["want"]
        assert Solution(c["in"]).inplace() == c["want"]
