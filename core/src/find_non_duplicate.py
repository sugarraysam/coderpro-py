from collections import defaultdict


# populate a hashmap, O(n) , n == len(xint), then read this hashmap and return val where d[va] == 1 O(n)
# linear time & space complexity
def sol_hashmap(xint):
    d = defaultdict(int)
    for i in xint:
        d[i] += 1

    for k, v in d.items():
        if v == 1:
            return k


# take advantage of the fact an int is present 2 or 1 time, use xor to cancel duplicates
# constant space complexity, time complexity linear
def sol_xor(xint):
    res = 0
    for i in xint:
        res ^= i
    return res
