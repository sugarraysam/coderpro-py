from core.src.ds_heap import MaxHeap


def test_max_heap():
    # integration tests
    heap = MaxHeap()
    for v in [2, 3, 6]:
        heap.insert(v)
        print(heap)
    assert heap.size == 3
    assert heap.first() == 6
    assert heap.last() == 3
    assert heap.pop() == 6
    assert heap.first() == 3
    assert heap.last() == 2
    for v in [9, 10, 1]:
        heap.insert(v)
        print(heap)
    assert heap.pop() == 10
    assert heap.first() == 9
    assert heap.last() == 1
    assert heap.size == 4
