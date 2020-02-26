from collections import defaultdict


class Calculator(object):
    """
    Calculator implementation using a stack.
    Receives infix expression, evaluates them by first doing a conversion to postfix.
    Supports parentheses.
    """

    def __init__(self, infix):
        self.infix = infix.replace(" ", "")
        self.ops = defaultdict(
            dict,
            {
                "(": {"rank": 3, "eval": None},
                ")": {"rank": 3, "eval": None},
                "*": {"rank": 2, "eval": lambda x, y: x * y},
                "/": {"rank": 2, "eval": lambda x, y: x / y},
                "+": {"rank": 1, "eval": lambda x, y: x + y},
                "-": {"rank": 1, "eval": lambda x, y: x - y},
            },
        )
        self.postfix = self._infix2postfix_v2()

    def _infix2postfix(self):
        postfix = []
        opstack = []
        for token in self.infix:
            if token == ")":
                op = opstack.pop()
                while op != "(":
                    postfix.append(op)
                    op = opstack.pop()

            elif self.ops[token]:
                # append if empty or top of stack is '('
                if not opstack or opstack[-1] == "(":
                    opstack.append(token)
                    continue
                p1 = self.ops[token]["rank"]
                p2 = self.ops[opstack[-1]]["rank"]
                if p1 >= p2:
                    opstack.append(token)
                else:
                    postfix.append(opstack.pop())
                    opstack.append(token)
            else:
                postfix.append(token)

        # empty opstack
        while opstack:
            postfix.append(opstack.pop())

        return "".join(postfix)

    def _infix2postfix_v2(self):
        postfix = []
        opstack = []
        for token in self.infix:
            if token == "(":
                opstack.append(token)
            elif token == ")":
                while opstack[-1] != "(":
                    postfix.append(opstack.pop())
                opstack.pop()  # discard "(" from opstack
            elif self.ops[token]:
                rank = self.ops[token]["rank"]
                while (
                    opstack
                    and opstack[-1] != "("
                    and self.ops[opstack[-1]]["rank"] > rank
                ):
                    postfix.append(opstack.pop())
                opstack.append(token)
            else:
                postfix.append(token)
        # empty opstack
        while opstack:
            postfix.append(opstack.pop())

        return "".join(postfix)

    def eval(self):
        stack = []
        for token in self.postfix:
            if self.ops[token]:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                stack.append(self.ops[token]["eval"](operand1, operand2))
            else:
                stack.append(token)
        return stack.pop()
