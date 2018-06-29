class Stack:
    def __init__(self):
        self.my_stack = []
    def empty(self):
        return len(self.my_stack) == 0
    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self.my_stack[-1][1]
    def push(self, x):
        if self.empty() or x > self.my_stack[-1][1]:
            self.my_stack.append((x, x))
        else:
            self.my_stack.append((x, self.my_stack[-1][1]))
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self.my_stack.pop()[0]

s = Stack()
s.push(17)
print(s.max())
s.push(20)
print(s.max())
s.push(25)
print(s.max())
s.pop()
print(s.max())
s.push(30)
print(s.max())
s.push(12)
print(s.max())
