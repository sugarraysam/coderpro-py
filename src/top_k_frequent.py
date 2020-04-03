import heapq
from collections import Counter, defaultdict

from src.ds_heap import MaxHeap


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
        """
        Solve using a min heap, sorting on count
        """
        if not self.nums or self.k == 0:
            return []

        counter = Counter(self.nums)
        return sorted(heapq.nlargest(self.k, counter.keys(), key=counter.get))

    def heap_oneliner(self):
        return sorted(
            [
                x[2]
                for x in heapq.nlargest(
                    self.k,
                    [
                        (count, i, val)
                        for (i, (val, count)) in enumerate(Counter(self.nums).items())
                    ],
                )
            ]
        )
