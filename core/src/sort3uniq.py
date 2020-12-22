from collections import defaultdict


def sol_hashmap(xint):
    vals = defaultdict(int)
    for i in xint:
        vals[i] += 1
    low, mid, high = sorted(vals.keys())
    return [low] * vals[low] + [mid] * vals[mid] + [high] * vals[high]


def sol_swap_inplace(xint):
    low = min(xint)
    high = max(xint)
    idx_low = idx = 0
    idx_high = len(xint) - 1
    while idx <= idx_high:
        if xint[idx] == low:
            xint[idx_low], xint[idx] = xint[idx], xint[idx_low]
            idx_low += 1
            idx += 1
        elif xint[idx] == high:
            xint[idx_high], xint[idx] = xint[idx], xint[idx_high]
            idx_high -= 1
        else:
            idx += 1
    return xint
