from src.ap46_invert_bintree import Node

TREE1 = Node(
    0,
    left=Node(1, left=Node(2), right=Node(3)),
    right=Node(4, left=Node(5), right=Node(6)),
)
TREE1_INV = Node(
    0,
    left=Node(4, left=Node(6), right=Node(5)),
    right=Node(1, left=Node(3), right=Node(2)),
)

TREE2 = Node(0, left=Node(1, left=Node(2, left=Node(3))))
TREE2_INV = Node(0, right=Node(1, right=Node(2, right=Node(3))))

TREE3 = Node(0, right=Node(1, right=Node(2, right=Node(3))))
TREE3_INV = Node(0, left=Node(1, left=Node(2, left=Node(3))))


def test_ap46_invert_bintree():
    cases = [
        {"in": TREE1, "want": TREE1_INV},
        {"in": TREE2, "want": TREE2_INV},
        {"in": TREE3, "want": TREE3_INV},
    ]
    for c in cases:
        c["in"].invert()
        assert c["in"] == c["want"]
