from src.intersection_two_ll import Node, Solution

NODE8 = Node(8, Node(4, Node(5)))
NODE2 = Node(2, Node(4))


def test_intersection_two_ll():
    cases = [
        {
            "L1": Node(4, Node(1, NODE8)),
            "L2": Node(5, Node(0, Node(1, NODE8))),
            "want": NODE8,
        },
        {"L1": Node(0, Node(9, Node(1, NODE2))), "L2": Node(3, NODE2), "want": NODE2},
        {"L1": None, "L2": None, "want": None},
        {"L1": Node(2, Node(6, Node(4))), "L2": Node(1, Node(5)), "want": None},
    ]
    for c in cases:
        sol = Solution(c["L1"], c["L2"])
        assert sol.set() == c["want"]
        assert sol.constant() == c["want"]
