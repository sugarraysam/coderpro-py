import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def quicksort(self):
        def _swap(i, j):
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        def _quicksort(start, end):
            print(f"DEBUG, {self.nums[start:end]}")
            # base case, only sort lists of 2+ elements
            if end - start <= 1:
                return
            pivot = random.choice(self.nums[start:end])
            left = start
            right = end - 1
            while left <= right:
                # find value > pivot
                while left < end and self.nums[left] < pivot:
                    left += 1
                # find value < pivot
                while right >= start and self.nums[right] > pivot:
                    right -= 1

                if left <= right:
                    _swap(left, right)
                    left += 1
                    right -= 1

            # quicksort low N high part
            _quicksort(start, left)
            _quicksort(right, end)

        # sort in place - empty case check
        if self.len > 1:
            _quicksort(0, self.len)
        return self.nums
