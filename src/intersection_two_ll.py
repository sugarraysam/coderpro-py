class Node(object):
    def __init__(self, val, nn=None):
        self.val = val
        self.next = nn

    def __eq__(self, other):
        return id(self) == id(other)

    def __hash__(self):
        return hash(id(self))

    def __repr__(self):
        s = f"Node({self.val})"
        curr = self
        while curr.next:
            curr = curr.next
            s = f"{s} -> Node({curr.val})"
        return s


class Solution(object):
    def __init__(self, L1, L2):
        self.L1 = L1
        self.L2 = L2

    def set(self):
        """
        Time complexity: O(max(len(L1), len(L2))
        Space complexity: O(max(len(L1), len(L2)))
        """
        # empty case
        if not self.L1 or not self.L2:
            return None

        seen = set()
        # traverse L1
        curr = self.L1
        while curr:
            seen.add(curr)
            curr = curr.next

        # traverse L2
        curr = self.L2
        while curr:
            # found intersection
            if curr in seen:
                return curr
            curr = curr.next

        # did not find intersection
        return None

    def _len(self, L):
        res = 0
        curr = L
        while curr:
            res += 1
            curr = curr.next
        return res

    def constant(self):
        """
        Time complexity: O(len(L1)) + O(len(L2)) + O(max(len(L1), len(L2)))
        Space complexity: O(1)
        """
        # empty case
        if not self.L1 or not self.L2:
            return None

        len_L1 = self._len(self.L1)
        len_L2 = self._len(self.L2)
        curr_L1 = self.L1
        curr_L2 = self.L2

        # synchronize
        if len_L1 > len_L2:
            for _ in range(len_L1 - len_L2):
                curr_L1 = curr_L1.next
        else:
            for _ in range(len_L2 - len_L1):
                curr_L2 = curr_L2.next

        # find intersection
        while curr_L1 and curr_L2:
            if curr_L1 is curr_L2:
                return curr_L1
            curr_L1 = curr_L1.next
            curr_L2 = curr_L2.next

        return None


if __name__ == "__main__":
    """
    Debugging
    """
    n1 = Node(1)
    n2 = n1
    n3 = Node(3)
    print(id(n1), id(n2), id(n3))
    if n1 is n2:
        print("equal")
    seen = set([n1, n2, n3])
    print([n in seen for n in [n1, n2, n3]])
