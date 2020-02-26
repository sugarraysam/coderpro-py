from src.course_schedule import Graph


def test_courses():
    cases = [
        {"in": {"num_courses": 2, "prerequisites": [[1, 0]]}, "want": True},
        {"in": {"num_courses": 2, "prerequisites": [[0, 1], [1, 0]]}, "want": False},
    ]
    for c in cases:
        assert (
            Graph(c["in"]["num_courses"], c["in"]["prerequisites"]).solution("bfs")
            == c["want"]
        )
        assert (
            Graph(c["in"]["num_courses"], c["in"]["prerequisites"]).solution("dfs")
            == c["want"]
        )
