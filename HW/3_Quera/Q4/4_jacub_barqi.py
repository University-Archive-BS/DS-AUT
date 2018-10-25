n, x = map(int, input().split())
stuff = input().split()

mid_sum_arr = []
mid_sum = 0
result = 0
for i in range(n):
    if mid_sum + int(stuff[i]) > x:
        mid_sum_arr.append(int(mid_sum))
        mid_sum = int(stuff[i])
    else:
        mid_sum += int(stuff[i])
mid_sum_arr.append(int(mid_sum))
print(mid_sum_arr)
for j in range(mid_sum_arr.__len__()):
    for k in range(j + 1, mid_sum_arr.__len__()):
        if mid_sum_arr[j] + mid_sum_arr[k] < x:
            mid_sum_arr[j] += mid_sum_arr[k]
            mid_sum_arr[k] = 0

print(mid_sum_arr)
for w in range(mid_sum_arr.__len__()):
    if mid_sum_arr[w] == 0:
        mid_sum_arr.pop(w)
print(mid_sum_arr.__len__())
