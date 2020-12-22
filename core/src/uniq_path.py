from math import factorial


class Solution(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def backtrack(self):
        """
        Time complexity: O(m * n), we populate every element of the grid
        Space complexity: O(m * n), we create a full grid
        """
        # empty case
        if self.m <= 1 or self.n <= 1:
            return 0

        grid = [[0] * self.n for _ in range(self.m)]

        for x in range(self.m):
            for y in range(self.n):
                # first row or first column
                if x == 0 or y == 0:
                    grid[x][y] = 1
                # value is addition of left and top values
                else:
                    grid[x][y] = grid[x][y - 1] + grid[x - 1][y]

        return grid[self.m - 1][self.n - 1]

    def singlerow(self):
        """
        Time complexity: O(m-1 * n-1), because first line initialized
        Space complexity: O(n), only using single row
        """
        # empty case
        if self.m <= 1 or self.n <= 1:
            return 0

        row = [1] * self.n
        for _ in range(1, self.m):
            for y in range(1, self.n):
                row[y] = row[y] + row[y - 1]

        return row[self.n - 1]

    def combinatory(self):
        """
        Time complexity: O(n) to calculate n!
        Space complexity: O(1), constant space

        Using combinatory approach, we know
            self.m - 1 + self.n - 1 is total number of moves (total choices)
            self.m - 1 is number of down moves to make
            self.n - 1 is number of right moves to make

        Calculate all posiibilities
        """
        if self.m <= 1 or self.n <= 1:
            return 0

        return factorial(self.m - 1 + self.n - 1) / (
            factorial(self.m - 1) * factorial(self.n - 1)
        )
