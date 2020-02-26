class Stack(object):
    def __init__(self):
        self.len = 0
        self.stack = []
        self.max = []  # latest value reflects current maximum

    def Push(self, value):
        # empty
        if not self.max:
            self.max.append(value)
        else:
            self.max.append(max(value, self.max[-1]))

        self.stack.append(value)
        self.len += 1

    def Pop(self):
        # empty
        if not self.stack:
            return None

        self.len -= 1
        _ = self.max.pop()  # discard current max
        return self.stack.pop()

    def Max(self):
        # empty
        if not self.max:
            return None

        return self.max[-1]

    def Len(self):
        return self.len
