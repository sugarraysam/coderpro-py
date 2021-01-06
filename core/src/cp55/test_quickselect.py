from core.src.cp55.quickselect import Quickselect
from collections import namedtuple
import pytest

Case = namedtuple("Case", "numbers k expected")


@pytest.mark.parametrize(
    "tc",
    [
        Case(numbers=[3, 2, 1, 5, 6, 4], k=2, expected=5),
        Case(numbers=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4, expected=4),
        Case(numbers=[4, 3, 5, 2, 0, 1], k=3, expected=3),
    ],
)
def test_solve(tc):
    assert Quickselect(tc.numbers.copy(), tc.k).solve_bruteforce() == tc.expected
    assert Quickselect(tc.numbers.copy(), tc.k).solve_sort() == tc.expected
