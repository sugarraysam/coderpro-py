# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Find the kth largest element in an unsorted array. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.


class Quickselect:
    def __init__(self, numbers, k):
        self.numbers = numbers
        self.k = k

    def solve_bruteforce(self):
        """
        Removes the largest element k times

        Time complexity:
            O(k * n), traverse array k times, assuming del array[k] is constant

        Space complexity:
            O(1), remove in place
        """
        max_value = -1
        for z in range(0, self.k):
            max_value = -1
            max_index = -1
            for i, v in enumerate(self.numbers):
                if v > max_value:
                    max_index = i
                    max_value = v
            del self.numbers[max_index]

        return max_value

    def solve_sort(self):
        """
        Sorts numbers in place then index

        Time complexity:
            O(n log n), sorting numbers

        Space complexity:
            O(1), sorting in place
        """
        if self.k < 0 or self.k > len(self.numbers):
            return None

        self.numbers.sort()  # in place
        return self.numbers[-self.k]

    def solve_quickselect(self):
        pass
