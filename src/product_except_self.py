class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def with_div(self):
        """
        Time complexity: O(n) get prod + O(n) create res = O(n)
        Space complexity: O(n) get res array
        """
        if not self.nums:
            return []
        if len(self.nums) == 1:
            return [0]

        prod = 1
        for n in self.nums:
            prod *= n

        return [prod // n for n in self.nums]

    def without_div(self):
        """
        Space complexity: O(n) R list + O(n) L list + O(n) res List == O(n)
        Time complexity: O(n) R list + O(n) L list + O(n) tres list == O(n)
        """
        if not self.nums:
            return []
        if len(self.nums) == 1:
            return [0]
        # get running prod on left
        left = []
        lval = 1
        for n in self.nums:
            left.append(lval)
            lval *= n

        # get running prod on right
        right = []
        rval = 1
        for n in self.nums[::-1]:
            right.append(rval)
            rval *= n
        right = right[::-1]

        res = []
        for i in range(len(self.nums)):
            res.append(left[i] * right[i])
        return res
