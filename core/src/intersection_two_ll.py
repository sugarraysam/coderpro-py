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
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def set(self):
        """
        Time complexity: O(max(len(A), len(B))
        Space complexity: O(max(len(A), len(B)))
        """
        # empty case
        if not self.A or not self.B:
            return None

        seen = set()
        # traverse A
        curr = self.A
        while curr:
            seen.add(curr)
            curr = curr.next

        # traverse B
        curr = self.B
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

    def _len2(self, L):
        # Tail recursive version
        def _len(node, acc):
            if node is None:
                return acc
            else:
                return _len(node.next, acc + 1)

        return _len(L, 0)

    def constant(self):
        """
        Time complexity: O(len(A)) + O(len(B)) + O(max(len(A), len(B)))
        Space complexity: O(1)
        """
        # empty case
        if not self.A or not self.B:
            return None

        # lenA, lenB = self._len(self.A), self._len(self.B)
        lenA, lenB = self._len2(self.A), self._len2(self.B)
        currA, currB = self.A, self.B

        # synchronize
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        # find intersection
        while currA and currB:
            if currA is currB:
                return currA
            currA = currA.next
            currB = currB.next

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
