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
command = []

for i in range(q):
    command.append(input())

for j in range(q):
    if command[j].__contains__("push"):
        push_array = command[j].split()
        element_stack = push_array[1]
        main_stack.push(element_stack)

        if min_stack.is_empty():
            min_stack.push(element_stack)
        else:
            element_min = min_stack.pop()
            min_stack.push(element_min)
            if element_stack <= element_min:
                min_stack.push(element_stack)

    if command[j].__contains__("pop"):
        element_stack = main_stack.pop()
        element_min = min_stack.pop()
        if element_min != element_stack:
            min_stack.push(element_min)

    if command[j].__contains__("spell"):
        element_min = min_stack.pop()
        print(element_min)
        min_stack.push(element_min)
