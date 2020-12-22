class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def height(self):
        def _helper(acc, node):
            # base case
            if node is None:
                return acc
            return max(_helper(acc + 1, node.left), _helper(acc + 1, node.right))

        return _helper(0, self)


class BinTree(object):
    def __init__(self, root):
        self.root = root

    def is_balanced_it(self):
        """
        Time complexity: O(n), where n is num of nodes in tree, if not balanced have to get all the way to the leaf
        Space complexity: O(n), call stack because using recursive calls to height
        """
        if self.root.left is None and self.root.right is None:
            return True
        elif self.root.left is None:
            return self.root.right.height() <= 1
        elif self.root.right is None:
            return self.root.left.height() <= 1
        else:
            return abs(self.root.left.height() - self.root.right.height()) <= 1

    def is_balanced_rec(self):
        """
        uses leftB and rightB to know if tree is balanced
        uses leftH and rightH to compute height of tree

        Time complexity: O(n)
        Space complexity: O(n)
        """

        def _helper(root):
            if root is None:
                return (True, 0)
            leftB, leftH = _helper(root.left)
            rightB, rightH = _helper(root.right)
            return (
                leftB and rightB and abs(leftH - rightH) <= 1,
                max(leftH, rightH) + 1,
            )

        return _helper(self.root)
