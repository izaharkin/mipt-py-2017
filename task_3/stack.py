import sys


class Stack:
    '''Imlpelemntation of stack.py'''

    def __init__(self, iterable=""):
        self.container = []
        for item in iterable:
            self.container.append(item)

    def push(self, item):
        self.container.append(item)

    def pop(self):
        self.container.pop()

    def top(self):
        return self.container[-1]

    def __len__(self):
        return len(self.container)

    def __str__(self):
        return " ".join(str(x) for x in self.container)


exec(sys.stdin.read())
