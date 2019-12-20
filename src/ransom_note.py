from collections import defaultdict


# Time complexity: O(n) -> n # letters in magazine, we go through them twice
# Space complexity: O(n) -> we store each letters in a dict len(n)
def can_construct(ransom, magazine):
    # default dict with letter count
    letters = defaultdict(int)
    for c in magazine:
        letters[c] += 1

    # validate ransom
    for c in ransom:
        letters[c] -= 1
        if letters[c] < 0:
            return False

    return True
