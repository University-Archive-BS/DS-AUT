class Stack:
    def __init__(self):
        self.list = []

    def push(self, element):
        self.list.append(element)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        if self.list.__len__() == 0:
            return True
        else:
            return False


stack_a = Stack()

temp = 0
q = int(input())

parentheses = list(str(input()))


beautifully = []

for i in parentheses:
    if i == '(':
        if stack_a.is_empty():
            temp = 0
        else:
            temp += 1
        stack_a.push(i)
    else:
        temp += 1
        stack_a.pop()
        # if stack_a.is_empty():
        #     temp += 1
        beautifully.append(temp)

print(max(beautifully))
