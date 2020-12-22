import pytest

from core.src.sort3uniq import sol_hashmap, sol_swap_inplace


@pytest.mark.parametrize("func", [sol_hashmap, sol_swap_inplace])
def test_sol_hashmap(func):
    cases = [
        {"in": [1, 3, 2, 1, 3, 2, 1], "want": [1, 1, 1, 2, 2, 3, 3]},
        {"in": [4, 7, 1, 4, 1, 1, 7], "want": [1, 1, 1, 4, 4, 7, 7]},
        {"in": [1, 1, 2, 5], "want": [1, 1, 2, 5]},
    ]
    for c in cases:
        assert func(c["in"]) == c["want"]
