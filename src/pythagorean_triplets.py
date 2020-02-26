from collections import defaultdict


class Solution:
    """
    Solve problem of finding pythagorean triplets
    Returns True if a triplet exists
    """

    def __init__(self, candidates):
        self.candidates = candidates

    # time complexity O(n^3), triple loop
    def naive(self):
        for a in self.candidates:
            for b in self.candidates:
                for c in self.candidates:
                    if a ** 2 + b ** 2 == c ** 2:
                        return True
        return False

    def hashmap(self):
        # populate hashmap with squares, time & space complexity O(n),
        squares = defaultdict(int, {i ** 2: i for i in self.candidates})

        # time complexity O(n^2)
        for a in self.candidates:
            for b in self.candidates:
                if squares[a ** 2 + b ** 2]:
                    return True
        return False

    def set(self):
        # populate set with squares, time & space complexity O(n)
        squares = set({i ** 2 for i in self.candidates})

        # double for loop find triplets - time complexity O(n**2)
        for a in self.candidates:
            for b in self.candidates:
                if a ** 2 + b ** 2 in squares:
                    return True
        return False
