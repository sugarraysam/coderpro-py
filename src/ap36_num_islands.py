class Islands(object):
    def __init__(self, grid):
        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def _sink(self, pos):
        """
        Sink an island using breadth first search algorithm,
        visiting all neighbors and turning them to zeroes.
        """
        neighbors = set([pos])
        while neighbors:
            x, y = neighbors.pop()
            # left
            if x - 1 >= 0 and self.grid[y][x - 1] == 1:
                neighbors.add((x - 1, y))
                self.grid[y][x - 1] = 0
            # right
            if x + 1 < self.width and self.grid[y][x + 1] == 1:
                neighbors.add((x + 1, y))
                self.grid[y][x + 1] = 0
            # top
            if y - 1 >= 0 and self.grid[y - 1][x] == 1:
                neighbors.add((x, y - 1))
                self.grid[y - 1][x] = 0
            # bottom
            if y + 1 < self.height and self.grid[y + 1][x] == 1:
                neighbors.add((x, y + 1))
                self.grid[y + 1][x] = 0

    def count(self):
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == 1:
                    count += 1
                    self._sink((x, y))

        return count
