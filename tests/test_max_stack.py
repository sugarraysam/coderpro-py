from src.max_stack import Stack


def test_stack_integration():
    stack = Stack()
    assert stack.Max() == None
    assert stack.Pop() == None
    assert stack.Len() == 0

    stack.Push(3)
    stack.Push(3)
    stack.Push(4)

    assert stack.Len() == 3
    assert stack.Max() == 4
    assert stack.Pop() == 4
    assert stack.Pop() == 3
    assert stack.Max() == 3

    _ = stack.Pop()
    _ = stack.Pop()
    _ = stack.Pop()

    assert stack.Len() == 0
    assert stack.Max() == None
