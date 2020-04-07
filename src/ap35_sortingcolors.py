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

    def hashmap(self):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if self.len < 2:
            return self.nums

        d = {0: 0, 1: 0, 2: 0}
        for n in self.nums:
            d[n] += 1

        return ([0] * d[0]) + ([1] * d[1]) + ([2] * d[2])

    def pointers(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self.len < 2:
            return self.nums
        next0, curr, next2 = 0, 0, self.len - 1

        while curr <= next2:
            if self.nums[curr] == 0:
                self._swap(next0, curr)
                next0 += 1
                curr += 1
            elif self.nums[curr] == 2:
                self._swap(next2, curr)
                next2 -= 1
            else:
                curr += 1

        return self.nums
