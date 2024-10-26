class StackEmptyError(Exception):
    def __str__(self):
        return "Stack is empty!"


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.length > 0:
            return self.data.pop()
        else:
            raise StackEmptyError()

    @property
    def length(self):
        return len(self.data)

    def peek(self):
        return self.data[-1]

    def clear(self):
        self.data.clear()

    def isempty(self):
        return len(self.data) == 0


s = Stack()
try:
    s.pop()
except ValueError as ex:
    print('Error -->' + str(ex))

s.push(10)
s.push(20)
print(s.peek())
print(s.pop())
print(s.length)  # property


# for v in s:
#     print(v)
