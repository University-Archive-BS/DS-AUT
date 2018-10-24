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

min = 0

for j in range(q):
    if command[j].__contains__("push"):
        push_array = command[j].split()
        element_stack = push_array[1]

        if main_stack.is_empty():
            min = element_stack
        elif element_stack < min:
            min = element_stack

        main_stack.push(element_stack)

    if command[j].__contains__("pop"):
        element_stack = main_stack.pop()
        if element_stack == min:
            temp = Stack()
            temp_element = main_stack.pop()
            min = temp_element
            main_stack.push(temp_element)
            while not main_stack.is_empty():
                temp_element = main_stack.pop()
                if temp_element < min:
                    min = temp_element
                temp.push(temp_element)
            while not temp.is_empty():
                main_stack.push(temp.pop())

    if command[j].__contains__("spell"):
        print(min)
