from src.top_k_frequent import Solution


def test_top_k_frequent():
    cases = [
        {"in": {"nums": [], "k": 2}, "want": []},
        {"in": {"nums": [1, 1, 2, 2, 3], "k": 2}, "want": [1, 2]},
        {"in": {"nums": [1, 1, 2, 2, 3], "k": 0}, "want": []},
        {"in": {"nums": [1, 1, 1, 2, 2, 3, 3, 4], "k": 4}, "want": [1, 2, 3, 4]},
    ]
    for c in cases:
        sol = Solution(c["in"]["nums"], c["in"]["k"])
        assert sol.counter() == c["want"]
        assert sol.hashmap() == c["want"]
        assert sol.heap() == c["want"]
        assert sol.heap_oneliner() == c["want"]
