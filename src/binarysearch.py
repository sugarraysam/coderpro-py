class BinarySearch(object):
    def __init__(self, nums):
        self.nums = nums

    def recursive(self, target):
        def _binarysearch(start, stop):
            # did not find target
            if start >= stop:
                return (False, -1)
            mid = (start + stop) // 2
            if target < self.nums[mid]:
                return _binarysearch(start, mid - 1)
            elif target > self.nums[mid]:
                return _binarysearch(mid + 1, stop)
            else:
                return (True, mid)

        return _binarysearch(0, len(self.nums))

    def iterative(self, target):
        start = 0
        stop = len(self.nums) - 1
        while start <= stop:
            mid = (start + stop) // 2
            if target > self.nums[mid]:
                start = mid + 1
            elif target < self.nums[mid]:
                stop = mid - 1
            else:
                return (True, mid)
        return (False, -1)
