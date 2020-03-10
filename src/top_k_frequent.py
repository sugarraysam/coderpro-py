import heapq
import itertools
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

        counter = itertools.count()
        most_freq = []
        # keep i as entry count for tie-breaker
        for val, count in Counter(self.nums).items():
            heapq.heappush(
                most_freq, (count, next(counter), val)
            )  # sort on count, then counter
            if len(most_freq) > self.k:
                heapq.heappop(most_freq)

        return sorted([heapq.heappop(most_freq)[2] for _ in range(self.k)])

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
