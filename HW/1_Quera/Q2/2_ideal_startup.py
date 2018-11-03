from collections import deque

queue = deque()

q = int(input())
command = []

for i in range(q):
    command.append(input())

last_command = ""
last_pop = 0

for j in range(q):
    if command[j].__contains__("enqueue"):
        push_array = command[j].split()
        element_queue = push_array[1]
        queue.append(element_queue)
        last_command = "enqueue"

    if command[j].__contains__("pop"):
        last_pop = queue.popleft()
        last_command = "pop"
        print(last_pop)

    if command[j].__contains__("undo"):
        if last_command == "enqueue":
            queue.pop()
        if last_command == "pop":
            queue.appendleft(last_pop)
