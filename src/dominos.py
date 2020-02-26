class Solution(object):
    def __init__(self, dominos):
        self.dominos = dominos
        self.len = len(dominos)

    # fill another array forces, summing left & right forces, than return interpretation
    # time complexity O(3n) , space complexity O(n)
    def numberalgo(self):
        # space complexity O(n)
        forces = [0] * self.len

        # Populate Rs, time complexity O(n)
        F = 0
        for i in range(self.len):
            if self.dominos[i] == "R":
                F = self.len
            elif self.dominos[i] == "L":
                F = 0
            else:
                F = max(0, F - 1)
            forces[i] += F

        # Populate Ls, time complexity O(n)
        F = 0
        for i in range(self.len - 1, -1, -1):
            if self.dominos[i] == "L":
                F = self.len
            elif self.dominos[i] == "R":
                F = 0
            else:
                F = max(0, F - 1)
            forces[i] -= F

        # Interpret forces in place, time complexity O(n)
        for i in range(self.len):
            if forces[i] == 0:
                forces[i] = "."
            elif forces[i] > 0:
                forces[i] = "R"
            else:
                forces[i] = "L"
        return "".join(forces)
