class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invert(self):
        def _invert(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            _invert(root.left)
            _invert(root.right)

        _invert(self)

    def __eq__(self, other):
        def _helper(curr, other):
            if curr is None:
                return curr == other
            return (
                curr.val == other.val
                and _helper(curr.left, other.left)
                and _helper(curr.right, other.right)
            )

        return _helper(self, other)
