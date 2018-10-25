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


main_stack = Stack()

q = int(input())
command = []

for i in range(q):
    command.append(input())

minimum = 0

for j in range(q):
    if command[j].__contains__("push"):
        push_array = command[j].split()
        element_stack = int(push_array[1])
        main_stack.push(element_stack)

    if command[j].__contains__("pop"):
        main_stack.pop()

    if command[j].__contains__("spell"):
        print(min(main_stack.list))
