from collections import Counter, defaultdict


class Solution(object):
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def counter(self):
        """
        Elements with equal counts are ordered in the order first encountered.
        """
        return [x[0] for x in Counter(self.nums).most_common(self.k)]

    def hashmap(self):
        hm = defaultdict(int)
        for n in self.nums:
            hm[n] += 1

        most_freq = [k for k, _ in sorted(hm.items(), key=lambda x: x[1], reverse=True)]
        return most_freq[: self.k]

    def heap(self):
        pass
