from collections import defaultdict
from queue import Queue


class Graph(object):
    def __init__(self, num_courses, prerequisites):
        self.algodict = {"bfs": self._bfs, "dfs": self._dfs}
        self.num_courses = num_courses
        self.visited = set()
        self.adjacency_list = defaultdict(list)
        for vertex in prerequisites:
            self.adjacency_list[vertex[0]].append(vertex[1])

    # False -> course combination not possible (cycle exists)
    # True -> course combination is possible (no cycle exist)
    def solution(self, algo):
        # visit graph setting every vertex as start point
        for i in range(self.num_courses):
            if self.algodict[algo](i):
                return False
        return True

    # True -> a cycle exists -- recursive
    def _dfs(self, v):
        self.visited.add(v)
        for neighbour in self.adjacency_list[v]:
            if neighbour in self.visited or self._dfs(neighbour):
                return True
        self.visited.remove(v)
        return False

    # True -> a cycle exists -- iterative
    def _bfs(self, v):
        tovisit = Queue()
        tovisit.put(v)
        while not tovisit.empty():
            vertex = tovisit.get()
            if vertex in self.visited:
                return True
            self.visited.add(vertex)
            for neighbour in self.adjacency_list[vertex]:
                tovisit.put(neighbour)
        self.visited = set()
        return False
