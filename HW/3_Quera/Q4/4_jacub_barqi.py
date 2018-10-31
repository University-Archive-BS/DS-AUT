from collections import deque

n, x = map(int, input().split())
stuffs = input().split()
stuffs.sort()
queue = deque()
for j in stuffs:
    queue.append(int(j))

boxes = 0
temp = 0
while temp != n:
    if queue.__len__() == 1:
        temp += 1
        boxes += 1
        break

    tail = queue.popleft()
    head = queue.pop()
    if head + tail <= int(x):
        boxes += 1
        temp += 2
    else:
        temp += 1
        boxes += 1
        queue.appendleft(tail)

print(boxes)
