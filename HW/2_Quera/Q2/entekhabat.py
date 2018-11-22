import heapq

n = int(input())
groups = input().split()
# groups.sort(key=int)

my_list = []
res = 0
for i in range(n):
    heapq.heappush(my_list, int(groups[i]))

print(my_list)
for j in range(n):
    if j == 0:
        res += heapq.heappop(my_list) * n
    else:
        res += heapq.heappop(my_list) * (n - j + 1)

print(res)
