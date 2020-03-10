class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.fixes = 0

    def solution(self):
        # empty case
        if len(self.nums) <= 1:
            return True

        for i in range(len(self.nums) - 1):
            prev = self.nums[i - 1] if i > 0 else None
            curr = self.nums[i]
            nxt = self.nums[i + 1]  # always exists

            # found a dip
            if nxt < curr:
                self.fixes += 1

                # two fixes
                if self.fixes == 2:
                    return False

                # dip on the right edge
                if i + 1 == len(self.nums) - 1:
                    return True

                # dip is too big
                if prev and nxt < prev:
                    return False

        return self.fixes <= 1
