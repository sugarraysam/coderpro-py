import collections

Node = collections.namedtuple("Node", "val left right")


class Solution:
    def __init__(self, tree):
        self.tree = tree

    def is_valid_bst(self) -> bool:
        def _helper(node, lower, upper):
            if not node:
                return True

            # check val
            val = node.val
            if val <= lower or val >= upper:
                return False

            # check left tree
            if not _helper(node.left, lower, val):
                return False
            if not _helper(node.right, val, upper):
                return False

            return True

        return _helper(self.tree, float("-inf"), float("inf"))


if __name__ == "__main__":
    # Validate code
    T1 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=4,
            left=Node(val=3, left=None, right=None),
            right=Node(val=6, left=None, right=None),
        ),
    )
    assert not Solution(T1).is_valid_bst()

    T2 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=6,
            left=Node(val=7, left=None, right=None),
            right=Node(val=8, left=None, right=None),
        ),
    )
    assert not Solution(T2).is_valid_bst()

    T3 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=6,
            left=Node(val=4, left=None, right=None),
            right=Node(val=7, left=None, right=None),
        ),
    )
    assert not Solution(T3).is_valid_bst()

    T4 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=7,
            left=Node(val=6, left=None, right=None),
            right=Node(val=8, left=None, right=None),
        ),
    )
    assert Solution(T4).is_valid_bst()
