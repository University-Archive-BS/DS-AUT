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
min_stack = Stack()

q = int(input())
commands = [''] * q

for i in range(q):
    commands[i] = input()

for j in range(q):
    if commands[j].__contains__("push"):
        push_array = commands[j].split()
        main_stack.push(push_array[1])

        if min_stack.is_empty():
            min_stack.push(push_array[1])
        else:
            element_min = min_stack.pop()
            min_stack.push(element_min)
            if push_array[1] < element_min:
                min_stack.push(push_array[1])

    if commands[j].__contains__("pop"):
        element_stack = main_stack.pop()
        element_min = min_stack.pop()
        if element_min != element_stack:
            min_stack.push(element_min)
    if commands[j].__contains__("spell"):
        element_min = min_stack.pop()
        print(element_min)
        min_stack.push(element_min)
