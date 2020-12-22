from core.src.valid_parentheses import Solution


def test_valid_parentheses():
    cases = [
        {"in": "", "want": True},
        {"in": "(){}[]", "want": True},
        {"in": "(([[{{}}]]))", "want": True},
        {"in": "(]", "want": False},
        {"in": "}", "want": False},
        {"in": "([{", "want": False},
    ]
    for c in cases:
        assert Solution(c["in"]).is_valid() == c["want"]
