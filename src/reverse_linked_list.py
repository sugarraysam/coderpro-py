class Node(object):
    def __init__(self, v, n=None):
        self.next = n
        self.value = v

    def __eq__(self, other):
        curr = self
        while curr.next:
            if not curr.value == other.value:
                return False
            curr = curr.next
            other = other.next
        return True

    def __repr__(self):
        out = ""
        curr = self
        while curr:
            out += f"Node({curr.value}) -> "
            curr = curr.next
        return out + "None"


class Solution(object):
    # time complexity linear, space complexity linear (creating new LinkedList)
    def naive(self, l):
        if l is None:
            return l
        curr = l
        head = Node(curr.value)
        while curr.next:
            curr = curr.next
            head = Node(curr.value, head)
        return head

    # time complexity linear, space complexity linear (creating new LinkedList)
    def recursion(self, l):
        if l is None:
            return l

        def _helper(l, acc):
            if l.next is None:
                return Node(l.value, acc)
            else:
                return _helper(l.next, Node(l.value, acc))

        return _helper(l, None)

    # time complexity linear, space complexity none because changing pointers inplace
    # use 3 pointers (mental trick: point to left)
    def inplace(self, l):
        curr = l
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
