# O(n) where n is len(xint), look for target in xint, linearly
def solNaive(xint, target):
    low, high = -1, -1
    for i, x in enumerate(xint):
        if x == target:
            low = i
            break
    if low == -1:
        return (low, high)
    else:
        high = low
        while high + 1 < len(xint) and xint[high + 1] == target:
            high += 1
        return (low, high)


# O(log(n)) where n is len(xint), use binary search
def solIterative(xint, target):
    low = binsearchIterative(xint, target, True)
    high = binsearchIterative(xint, target, False)
    return (low, high)


def solRecursive(xint, target):
    low = 0
    high = len(xint) - 1
    low = binsearchRecursive(xint, target, low, high, True)
    high = binsearchRecursive(xint, target, low, high, False)
    return (low, high)


# iterative binary search implementation
def binsearchIterative(xint, target, first):
    low = 0
    high = len(xint) - 1
    while low <= high:
        mid = (low + high) // 2
        if xint[mid] > target:
            high = mid - 1
        elif xint[mid] < target:
            low = mid + 1
        else:
            if first:
                while mid - 1 >= 0 and xint[mid - 1] == target:
                    mid -= 1
            else:
                while mid + 1 < len(xint) and xint[mid + 1] == target:
                    mid += 1
            return mid
    return -1


# recursive binary search implementation
def binsearchRecursive(xint, target, low, high, first):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif xint[mid] > target:
        return binsearchRecursive(xint, target, low, mid - 1, first)
    elif xint[mid] < target:
        return binsearchRecursive(xint, target, mid + 1, high, first)
    else:
        if first:
            while mid - 1 >= 0 and xint[mid - 1] == target:
                mid -= 1
        else:
            while mid + 1 < len(xint) and xint[mid + 1] == target:
                mid += 1
        return mid
