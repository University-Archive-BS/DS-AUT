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

        if main_stack.is_empty():
            minimum = element_stack
            main_stack.push(element_stack)
        else:
            if minimum <= element_stack:
                main_stack.push(element_stack)
            else:
                main_stack.push((2 * element_stack) - minimum)
                minimum = element_stack

    if command[j].__contains__("pop"):
        pop_element = main_stack.pop()
        if minimum > pop_element:
            minimum = (2 * minimum) - pop_element

    if command[j].__contains__("spell"):
        print(minimum)
