class Stack:
    def __init__(self):
        self.list = []
        self.minimum = 0

    def push(self, element):
        if self.is_empty:
            self.minimum = element
            self.list.append(element)
        else:
            if self.minimum <= element:
                self.list.append(element)
            else:
                self.minimum = element
                self.list.append(element)

    def pop(self):
        return self.list.pop()

    def spell(self):
        return self.minimum

    def is_empty(self):
        if self.list.__len__() == 0:
            return True
        else:
            return False


stack = Stack()
q = int(input())
commands = [''] * q
for i in range(q):
    commands[i] = input()

for j in range(q):
    if commands[j].__contains__("push"):
        push_array = commands[j].split()
        stack.push(push_array[1])
        print(push_array[1])
    if commands[j].__contains__("pop"):
        # print("pop " + stack.pop())
        stack.pop()
    if commands[j].__contains__("spell"):
        print("spell " + stack.spell())
