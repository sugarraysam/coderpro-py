import pytest

from src.find_non_duplicate import sol_hashmap, sol_xor


@pytest.mark.parametrize("func", [sol_hashmap, sol_xor])
def test_sol(func):
    cases = [{"in": [1, 1, 2, 4, 4, 6, 6], "want": 2}]
    cases = [{"in": [3, 3, 7, 9, 9], "want": 7}]
    for c in cases:
        assert func(c["in"]) == c["want"]
