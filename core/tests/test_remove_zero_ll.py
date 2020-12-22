from core.src.remove_zero_ll import Node, Solution


def test_remove_zero_ll():
    cases = [
        {"in": Node(1, Node(2, Node(-3, Node(3, Node(1))))), "want": Node(3, Node(1))},
        {
            "in": Node(1, Node(2, Node(3, Node(-3, Node(4))))),
            "want": Node(1, Node(2, Node(4))),
        },
        {"in": Node(1, Node(2, Node(3, Node(-3, Node(-2))))), "want": Node(1)},
        {"in": None, "want": None},
    ]
    for c in cases:
        assert Solution(c["in"]).solution() == c["want"]
