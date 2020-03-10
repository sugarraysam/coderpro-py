import math


class MaxHeap(object):
    def __init__(self):
        self.size = 0
        self.cap = 10
        self.nums = [0] * self.cap

    def _parent(self, i):
        idx = math.ceil((i - 2) / 2)
        return idx if i > 0 and self.nums else None

    def _left_child(self, i):
        idx = i * 2 + 1
        return idx if idx < self.size else None

    def _right_child(self, i):
        idx = i * 2 + 2
        return idx if idx < self.size else None

    def _swap(self, i, j):
        print(f"DEBUG: swapping {i} with {j}")
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def _ensure_capacity(self):
        if self.size == self.cap:
            self.cap *= 2
            self.nums = self.nums[:] + [0] * (self.cap - self.size)

    def _heapify_up(self):
        """
        Swap last element with parent while larger
        """
        idx = self.size - 1
        while (
            self._parent(idx) is not None
            and self.nums[idx] > self.nums[self._parent(idx)]
        ):
            self._swap(self._parent(idx), idx)
            idx = self._parent(idx)

    def _heapify_down(self):
        """
        Swap root going down with largest child
        """
        idx = 0
        while self._left_child(idx):
            # find largest child
            largest_child = self._left_child(idx)
            if (
                self._right_child(idx)
                and self.nums[self._right_child(idx)] > self.nums[self._left_child(idx)]
            ):
                largest_child = self._right_child(idx)

            # done
            if self.nums[largest_child] > self.nums[idx]:
                self._swap(largest_child, idx)
                idx = largest_child
            else:
                break

    def pop(self):
        item = self.nums[0]
        self.nums[0] = self.nums[self.size - 1]  # dont need to delete elem
        self.size -= 1
        self._heapify_down()
        return item

    def insert(self, elem):
        self._ensure_capacity()
        self.nums[self.size] = elem
        self.size += 1
        self._heapify_up()

    def first(self):
        if not self.nums:
            return None
        else:
            return self.nums[0]

    def last(self):
        if not self.nums:
            return None
        else:
            return self.nums[self.size - 1]

    def __repr__(self):
        return f"MaxHeap(nums: {self.nums}, size: {self.size}, cap: {self.cap})"
