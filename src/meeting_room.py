class Solution(object):
    def __init__(self, times):
        self.times = times

    def sorting(self):
        """
        Time complexity: O(n logn) to sort array, also O(2n), traverse it twice
        Space complexity: O(n), alltimes array
        """
        rooms = 0

        # read all times and sort
        alltimes = []
        for t in self.times:
            alltimes.append((t[0], True))
            alltimes.append((t[1], False))
        alltimes.sort()

        # find rooms required
        curr = 0
        for _, isstart in alltimes:
            if isstart:
                curr += 1
                rooms = max(curr, rooms)
            else:
                curr -= 1
        return rooms
