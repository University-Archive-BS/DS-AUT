n, x = map(int, input().split())
stuffs = input().split()
stuffs.sort()

boxes = 0
tail = stuffs.__len__() - 1
head = 0
temp = 0
while temp != n:
    # print(int(stuffs[head]) + int(stuffs[tail]))
    if head == tail:
        temp += 1
        boxes += 1
        # print("if " + str(boxes))
    elif int(stuffs[head]) + int(stuffs[tail]) <= int(x):
        boxes += 1
        head += 1
        tail -= 1
        temp += 2
        # print("elif " + str(boxes))
    else:
        temp += 1
        boxes += 1
        tail -= 1
        # print("else " + str(boxes))

print(boxes)
