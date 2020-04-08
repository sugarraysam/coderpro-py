from src.ap46_invert_bintree import Node
from copy import deepcopy

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
        {"in": Node(0), "want": Node(0)},
        {"in": TREE1, "want": TREE1_INV},
        {"in": TREE2, "want": TREE2_INV},
        {"in": TREE3, "want": TREE3_INV},
    ]
    for c in cases:
        # recursion
        c_rec = deepcopy(c["in"])
        c_rec.invert_rec()
        assert c_rec == c["want"]

        # iterative
        c_it = deepcopy(c["in"])
        c_it.invert_it()
        assert c_it == c["want"]
