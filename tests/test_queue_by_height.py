from src.queue_by_height import sol


def test_sol():
    cases = [
        {
            "in": [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            "want": [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        },
    ]
    for c in cases:
        assert sol(c["in"]) == c["want"]
