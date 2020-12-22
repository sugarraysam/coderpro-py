from core.src.gen_paren import Solution


def test_gen_paren():
    cases = [
        {"in": 3, "want": ["((()))", "(()())", "(())()", "()(())", "()()()"]},
    ]
    for c in cases:
        assert Solution(c["in"]).backtrack() == c["want"]
