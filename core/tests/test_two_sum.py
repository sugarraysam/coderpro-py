from core.src.two_sum import two_sum


def test_two_sum():
    # TODO more cases
    cases = [
        {"xi": [2, 7, 11, 15], "target": 9, "want": [0, 1]},
    ]
    for c in cases:
        # TODO list equality works?
        assert two_sum(c["xi"], c["target"]) == c["want"]
