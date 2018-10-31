n, x = map(int, input().split())
stuffs = input().split()
stuffs.sort()

temp = 0
tail = stuffs.__len__() - 1
head = 0
while head != tail:
    if int(stuffs[head]) + int(stuffs[tail]) <= x:
        temp += 1
        head += 1
        tail -= 1
    else:
        temp += 1
        head += 1


print(temp)
