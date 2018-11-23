import heapq

n = int(input())
groups = input().split()

my_list = []
res = 0
for i in range(n):
    heapq.heappush(my_list, int(groups[i]))

temp = 0
while my_list.__len__() > 1:
    temp = heapq.heappop(my_list)
    temp += heapq.heappop(my_list)
    res += temp
    heapq.heappush(my_list, temp)

res += temp
print(res)
