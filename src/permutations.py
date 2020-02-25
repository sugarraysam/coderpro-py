# returns n! permutations as a list of list, using backtracking and recursion
def sol(xint):
    res = []

    def _helper(start):
        # base case
        if start == len(xint) - 1:
            res.append(xint.copy())
        for i in range(start, len(xint)):
            xint[start], xint[i] = xint[i], xint[start]
            _helper(start + 1)
            xint[start], xint[i] = xint[i], xint[start]

    _helper(0)
    return res
