from src.dominos import Solution


def test_dominoes():
    cases = [
        {"in": ".L.R...LR..L..", "want": "LL.RR.LLRRLL.."},
        {"in": "RR.L", "want": "RR.L"},
    ]
    for c in cases:
        sol = Solution(c["in"])
        assert sol.numberalgo() == c["want"]
