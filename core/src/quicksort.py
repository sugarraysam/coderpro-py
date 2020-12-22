class Quicksort(object):
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def recursive_new(self):
        """
        Recursive implementation, creates new list.
        Time complexity: O(n log n)
        Space complexity: O(n)
        """

        def _helper(nums):
            if len(nums) <= 1:
                return nums
            else:
                p = nums.pop()  # need to pop, else we analyze pivot twice
                lt = []
                gt = []
                for n in nums:
                    if n <= p:
                        lt.append(n)
                    else:
                        gt.append(n)
                return _helper(lt) + [p] + _helper(gt)

        return _helper(self.nums.copy())

    def recursive_inplace(self):
        """
        Not creating a new list, swapping self.nums directly
        Time complexity: O(n log n)
        Space complexity: constant
        """

        def _helper(start, stop):
            if stop - start > 0:
                pivot, left, right = self.nums[start], start, stop
                while left <= right:
                    while self.nums[left] < pivot:
                        left += 1
                    while self.nums[right] > pivot:
                        right -= 1
                    if left <= right:
                        self.nums[left], self.nums[right] = (
                            self.nums[right],
                            self.nums[left],
                        )
                        left += 1
                        right -= 1
                _helper(start, right)
                _helper(left, stop)

        _helper(0, self.len - 1)
        return self.nums
