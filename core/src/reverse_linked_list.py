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
    def naive(self, ll):
        if ll is None:
            return ll
        curr = ll
        head = Node(curr.value)
        while curr.next:
            curr = curr.next
            head = Node(curr.value, head)
        return head

    # time complexity linear, space complexity linear (creating new LinkedList)
    def recursion(self, ll):
        if ll is None:
            return ll

        def _helper(ll, acc):
            if ll.next is None:
                return Node(ll.value, acc)
            else:
                return _helper(ll.next, Node(ll.value, acc))

        return _helper(ll, None)

    # time complexity linear, space complexity none because changing pointers inplace
    # use 3 pointers (mental trick: point to left)
    def inplace(self, ll):
        curr = ll
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
