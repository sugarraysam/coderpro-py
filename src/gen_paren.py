class Solution(object):
    def __init__(self, n):
        self.n = n

    def backtrack(self):
        res = []

        def _backtrack(s, left, right):
            # base case
            if len(s) == 2 * self.n:
                res.append(s)
                return
            # can still append left parentheses
            if left < self.n:
                _backtrack(f"{s}(", left + 1, right)
            # can append right parentheses
            if right < left:
                _backtrack(f"{s})", left, right + 1)

        _backtrack("", 0, 0)
        return res
