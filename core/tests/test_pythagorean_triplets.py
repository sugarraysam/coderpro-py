from core.src.pythagorean_triplets import Solution


def test_pythagorean_triplets_bool():
    cases = [{"in": [3, 5, 12, 5, 13], "want": True}]
    for c in cases:
        sol = Solution(c["in"])
        assert sol.naive() == c["want"]
        assert sol.hashmap() == c["want"]
        assert sol.set() == c["want"]
