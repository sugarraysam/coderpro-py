from collections import defaultdict


class Triplet(object):
    """
    Custom class to validate Triplets are uniq
    """

    def __init__(self, vals):
        self.triplet = sorted(vals)

    def __eq__(self, other):
        return (
            self.triplet[0] == other.triplet[0]
            and self.triplet[1] == other.triplet[1]
            and self.triplet[2] == other.triplet[2]
        )

    def __lt__(self, other):
        return (
            self.triplet[0] < other.triplet[0]
            or self.triplet[1] < other.triplet[1]
            or self.triplet[2] < other.triplet[2]
        )

    def __repr__(self):
        return (
            f"Triplet(a: {self.triplet[0]}, b: {self.triplet[1]}, c: {self.triplet[2]})"
        )


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def hashmap(self):
        """
        Time complexity: O(n^2) to create duos, then O(n) to find matches, total O(n^2)
        Space complexity: O(n^2) potential duos in dictionary + res max of O(n/3) , total O(n^2)
        """
        res = []

        # find potential duos, make sure dont double (i,j) == (j,i)
        duos = defaultdict(list)
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                duos[self.nums[i] + self.nums[j]].append(set((i, j)))

        # find triplet
        for k in range(len(self.nums)):
            # a + b + c = 0 <==> a + b == -c
            for duo in duos[-self.nums[k]]:
                # uniq indexes
                if k not in duo:
                    i, j = list(duo)
                    # print(f"DEBUG: found (i,j,k): ({i}, {j}, {k}) in set: {duo}")
                    triplet = Triplet((self.nums[x] for x in (i, j, k)))
                    if triplet not in res:
                        res.append(triplet)

        return res

    def inplace(self):
        """
        Time complexity: O(n^2), for each number, run _twosums which is O(n), so n * n == n^2
        Space complexity: inplace, using pointers on array, and sorting in place , O(1)
        """

        def _twosum(target, left, right):
            """
            find a,b such that a + b = target,  where target == -c
            return a list of potential triplets
            """
            res = []
            while left < right:
                total = self.nums[left] + self.nums[right]
                # lower than target: increment left pointer
                if total < target:
                    left += 1
                # greater than target: decrement right pointer
                elif total > target:
                    right -= 1
                # found a match
                else:
                    triplet = Triplet((-target, self.nums[left], self.nums[right]))
                    if triplet not in res:
                        res.append(triplet)
                    left += 1

            return res

        res = []
        self.nums.sort()  # only works with sorted list !!! O(n log n)
        for i in range(len(self.nums) - 2):
            target = -self.nums[i]
            for triplet in _twosum(target, i + 1, len(self.nums) - 1):
                if triplet not in res:
                    res.append(triplet)

        return sorted(res)
