from core.src.add_linked_list import (
    Node,
    add_linked_list_iterative,
    add_linked_list_recursive,
)


def _get_cases():
    # Build lists
    L123 = Node(1)
    L123.next = Node(2)
    L123.next.next = Node(3)

    L456 = Node(4)
    L456.next = Node(5)
    L456.next.next = Node(6)

    L789 = Node(7)
    L789.next = Node(8)
    L789.next.next = Node(9)

    L579 = Node(5)
    L579.next = Node(7)
    L579.next.next = Node(9)

    L8031 = Node(8)
    L8031.next = Node(0)
    L8031.next.next = Node(3)
    L8031.next.next.next = Node(1)

    # Build and return cases
    return [
        {"L1": None, "L2": None, "want": None},
        {"L1": L123, "L2": L456, "want": L579},
        {"L1": L123, "L2": L789, "want": L8031},
    ]


def test_recursive():
    cases = _get_cases()

    for c in cases:
        got = add_linked_list_recursive(c["L1"], c["L2"])
        want = c["want"]
        while got:
            assert got.val == want.val
            got = got.next
            want = want.next


def test_iterative():
    cases = _get_cases()

    for c in cases:
        got = add_linked_list_iterative(c["L1"], c["L2"])
        want = c["want"]
        while got:
            assert got.val == want.val
            got = got.next
            want = want.next
