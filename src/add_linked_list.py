class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# let n be len of largest list
# Space complexity: O(n) (call stack)
# Time complexity: O(n)
def add_linked_list_recursive(L1, L2):
    head = None

    def helper(L1, L2, carry, acc):
        # No more values, add carry if exists
        if L1 is None and L2 is None:
            if carry:
                acc.next = Node(1)
            return acc

        # L1 is empty, default to 0
        if L1 is None:
            val1, val2 = 0, L2.val
            L2 = L2.next

        # L2 is empty, default to 0
        if L2 is None:
            val1, val2 = L1.val, 0
            L1 = L1.next

        # L1 and L2 have values
        if L1 and L2:
            val1, val2 = L1.val, L2.val
            L1, L2 = L1.next, L2.next

        # Recursive call with accumulator
        total = val1 + val2 + carry
        if acc is None:
            head = Node(total % 10)
            acc = head
        else:
            acc.next = Node(total % 10)
            acc = acc.next
        return helper(L1, L2, total // 10, acc)

    # Define and return head pointer
    _ = helper(L1, L2, 0, None)
    return head


# Space complexity: constant
# Time complexity: O(n)
def add_linked_list_iterative(L1, L2):
    head, curr = None, None
    total = 0
    carry = 0
    val1, val2 = 0, 0

    # Iterate through both lists
    while L1 or L2:
        # L1 no more vals
        if L1 is None:
            val1, val2 = 0, L2.val
            L1, L2 = L1, L2.next

        # L2 no more vals
        if L2 is None:
            val1, val2 = L1.val, 0
            L1, L2 = L1.next, L2

        # L1 and L2 have vals
        if L1 and L2:
            val1, val2 = L1.val, L2.val
            L1, L2 = L1.next, L2.next

        print(f"DEBUG: val1 {val1} + val2 {val2} + carry {carry}")
        total = val1 + val2 + carry
        carry = total // 10
        if curr is None:
            head = Node(total % 10)
            curr = head
        else:
            curr.next = Node(total % 10)
            curr = curr.next

    # No more values, check carry and return head of the list
    if carry:
        curr.next = Node(1)
    return head
