from core.src.ransom_note import can_construct


def test_can_construct():
    assert not can_construct("a", "b")
    assert not can_construct("aa", "ab")
    assert can_construct("aa", "aab")
