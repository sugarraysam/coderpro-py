from core.src.cp38_balanced_bintree import Node, BinTree


def test_38_balanced_bintree():
    cases = [
        {"in": Node(0), "want": True},
        {"in": Node(0, Node(1), Node(2)), "want": True},
        {"in": Node(0, left=Node(1, left=Node(2, left=Node(3)))), "want": False},
        {"in": Node(0, right=Node(1, right=Node(2, right=Node(3)))), "want": False},
        {
            "in": Node(
                0,
                left=Node(1, left=Node(2, left=Node(3), right=Node(4)), right=Node(3)),
                right=Node(5, left=Node(6), right=Node(7)),
            ),
            "want": True,
        },
        {
            "in": Node(
                0,
                left=Node(
                    1,
                    left=Node(2, left=Node(3), right=Node(4)),
                    right=Node(3, right=Node(10)),
                ),
                right=Node(5, left=Node(6), right=Node(7)),
            ),
            "want": False,
        },
    ]
    for c in cases:
        BinTree(c["in"]).is_balanced_it() == c["want"]
        BinTree(c["in"]).is_balanced_rec() == c["want"]
