from core.src.cp36_num_islands import Islands
from copy import deepcopy


def test_ap36_num_islands():
    cases = [
        {"in": [[]], "want": 0},
        {"in": [[0], [0], [0]], "want": 0},
        {"in": [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]], "want": 1},
        {"in": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], "want": 3},
        {"in": [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]], "want": 4},
        {"in": [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]], "want": 5},
        {"in": [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]], "want": 4},
    ]
    for c in cases:
        Islands(deepcopy(c["in"])).count() == c["want"]
