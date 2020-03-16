from src.meeting_room import Solution


def test_meeting_room():
    cases = [
        {"in": [], "want": 0},
        {"in": [[0, 30], [5, 10], [15, 20]], "want": 2},
        {"in": [[7, 10], [2, 4]], "want": 1},
    ]
    for c in cases:
        sol = Solution(c["in"])
        assert sol.sorting() == c["want"]
