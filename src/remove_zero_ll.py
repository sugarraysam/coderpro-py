from collections import OrderedDict


class Node(object):
    def __init__(self, val, nn=None):
        self.val = val
        self.next = nn

    def __eq__(self, other):
        curr1 = self
        curr2 = other
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return curr1 is None and curr2 is None

    def __repr__(self):
        curr = self
        s = f"Node({curr.val})"
        while curr.next:
            curr = curr.next
            s = f"{s} -> Node({curr.val})"
        return s


class Solution(object):
    def __init__(self, head):
        self.head = head

    def solution(self):
        """
        Time complexity: O(n), where n is len(linked_list), we go over the list once
        Space complexity: O(n), at max we store "n" number in seen hashmap
        """
        if not self.head:
            return None

        dummy = curr = Node(0, self.head)
        psum = 0
        seen = OrderedDict()
        while curr:
            psum += curr.val

            if psum not in seen:
                seen[psum] = curr
            else:
                # pop until get node
                val = seen.popitem()
                while val[0] != psum:
                    val = seen.popitem()

                val[1].next = curr.next

            curr = curr.next

        return dummy.next
