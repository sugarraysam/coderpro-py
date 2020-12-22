import pytest

from core.src.reverse_linked_list import Node, Solution

LIST1 = Node(0, Node(1, Node(2, Node(3))))
REVLIST1 = Node(3, Node(2, Node(1, Node(0))))

LIST2 = Node(2, Node(4, Node(1, Node(5))))
REVLIST2 = Node(5, Node(1, Node(4, Node(2))))

LIST3 = Node(0)
REVLIST3 = Node(0)


@pytest.mark.parametrize(
    "func", [Solution().naive, Solution().recursion, Solution().inplace]
)
def test_sol(func):
    cases = [
        {"in": LIST1, "want": REVLIST1},
        {"in": LIST2, "want": REVLIST2},
        {"in": LIST3, "want": REVLIST3},
        {"in": None, "want": None},
    ]
    for c in cases:
        assert func(c["in"]) == c["want"]
