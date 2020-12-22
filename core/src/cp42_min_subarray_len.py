class SubArray(object):
    def __init__(self, nums, s):
        self.nums = nums
        self.s = s

    def naive(self):
        """
        Time complexity: O(n**2), visit every position, and for each position visit each position (worst case)
        Space complexity: O(1)
        """
        # init res to impossible high value
        res = len(self.nums) * 3
        for i in range(len(self.nums)):
            j, sub = i, 0
            while j < len(self.nums) and sub < self.s:
                sub += self.nums[j]
                j += 1

            if sub >= self.s:
                res = min(j - i, res)

        return 0 if res > len(self.nums) else res

    def pointers(self):
        """
        Time complexity: O(n), we go through array only once using 2 pointers
        Space complexity: O(1)
        """
        # empty case
        if not self.nums:
            return 0

        res = len(self.nums) * 3
        left, right, sub = 0, 0, 0

        while right < len(self.nums):
            sub += self.nums[right]
            while sub >= self.s:
                res = min(right - left + 1, res)
                sub -= self.nums[left]
                left += 1
            right += 1

        return 0 if res > len(self.nums) else res
