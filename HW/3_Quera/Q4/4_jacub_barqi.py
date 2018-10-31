n, x = map(int, input().split())
stuffs = input().split()
stuffs.sort()

boxes = 0
tail = stuffs.__len__() - 1
head = 0
temp = 0
while temp != n:
    if head == tail:
        temp += 1
        boxes += 1
    elif int(stuffs[head]) + int(stuffs[tail]) <= x:
        boxes += 1
        head += 1
        tail -= 1
        temp += 2
    else:
        temp += 1
        boxes += 1
        head += 1


print(boxes)
