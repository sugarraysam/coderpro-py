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
