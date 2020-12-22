from core.src.binary_search_tree import Node, Solution


def test_trees():
    # Create trees
    T1 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=4,
            left=Node(val=3, left=None, right=None),
            right=Node(val=6, left=None, right=None),
        ),
    )
    T2 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=6,
            left=Node(val=7, left=None, right=None),
            right=Node(val=8, left=None, right=None),
        ),
    )
    T3 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=6,
            left=Node(val=4, left=None, right=None),
            right=Node(val=7, left=None, right=None),
        ),
    )
    T4 = Node(
        val=5,
        left=Node(val=1, left=None, right=None),
        right=Node(
            val=7,
            left=Node(val=6, left=None, right=None),
            right=Node(val=8, left=None, right=None),
        ),
    )
    # Validate
    assert not Solution(T1).is_valid_bst()
    assert not Solution(T2).is_valid_bst()
    assert not Solution(T3).is_valid_bst()
    assert Solution(T4).is_valid_bst()
