class SubArray(object):
    def __init__(self, nums):
        self.nums = nums

    def naive(self):
        """
        Time complexity: O(n**2)
        Space complexity: O(1)
        """
        if not self.nums:
            return 0

        res = self.nums[0]
        for i in range(len(self.nums)):
            curr = self.nums[i]
            for j in range(i + 1, len(self.nums)):
                curr += self.nums[j]
                res = max(curr, res)

        return res

    def linear(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not self.nums:
            return 0

        res = self.nums[0]
        curr = 0
        for n in self.nums:
            curr += n
            if curr < 0:
                curr = 0
                res = max(res, n)
            else:
                res = max(res, curr)

        return res
