# sort by height (reversed), than by how many people they see
def sol(people):
    # sort people inplace, with 2 conditions in decreasing order of priority
    people.sort(key=lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        # insert(index, object) before given index
        res.insert(p[1], p)
    return res
