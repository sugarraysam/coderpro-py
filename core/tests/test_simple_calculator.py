from core.src.simple_calculator import Calculator


def test_calculator_infix_to_postfix():
    cases = [
        {"in": "A + B - C", "want": "ABC-+"},
        {"in": "A + B * C", "want": "ABC*+"},
        {"in": "A + B * C / D", "want": "ABCD/*+"},
        {"in": "A * B - C / D", "want": "AB*CD/-"},
        {"in": "A * (B - C) / D", "want": "ABC-D/*"},
        {"in": "(A + B) * (C - D * B - E)", "want": "AB+CDB*E--*"},
    ]
    for c in cases:
        calc = Calculator(c["in"])
        assert calc.postfix == c["want"]


def test_calculator():
    cases = [
        {"in": "1 + 3 - 4", "want": 0},
        {"in": "1 + 3 * 4", "want": 13},
        {"in": "1 + 3 * 4 / 2", "want": 7},
        {"in": "1 * 3 - 4 / 2", "want": 1},
        {"in": "(1 + 3) * (4 - 2 * 3 - 7)", "want": 20},
    ]
    for c in cases:
        calc = Calculator(c["in"])
        assert calc.eval() == c["want"]
