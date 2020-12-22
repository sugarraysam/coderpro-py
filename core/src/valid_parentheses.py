class Solution(object):
    def __init__(self, parentheses):
        self.parentheses = parentheses
        self.stack = []
        self.closing = set([")", "}", "]"])
        self.match = dict({")": "(", "]": "[", "}": "{"})

    def is_valid(self):
        """
        Time complexity: O(n) go through all elements once
        Space complexity: O(n) store all elements in stack
        """
        for par in self.parentheses:
            if par in self.closing:
                # empty stack
                if len(self.stack) == 0:
                    return False
                # unmatched parentheses
                elif self.stack.pop() != self.match[par]:
                    return False
            else:
                # push opening par
                self.stack.append(par)

        # make sure stack is empty
        return len(self.stack) == 0
