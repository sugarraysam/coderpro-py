import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def _swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def bubble(self):
        """
        Time complexity: O(n^2)
        Space complexity: O(1) - inplace
        """
        for i in range(self.len):
            for j in range(i + 1, self.len):
                if self.nums[j] < self.nums[i]:
                    self._swap(j, i)
        return self.nums

    def quicksort(self):
        """
        Time complexity: O(nlogn)
        Space complexity: O(1) - inplace
        """

        def _quicksort(start, end):
            # base case, only sort lists of 2+ elements
            if end - start < 1:
                return
            pivot, left, right = random.choice(self.nums[start : end + 1]), start, end
            while left <= right:
                # find value > pivot
                while self.nums[left] < pivot:
                    left += 1
                # find value < pivot
                while self.nums[right] > pivot:
                    right -= 1
                # swap
                if left <= right:
                    self._swap(left, right)
                    left += 1
                    right -= 1
            _quicksort(start, right)
            _quicksort(left, end)

        _quicksort(0, self.len - 1)
        return self.nums
