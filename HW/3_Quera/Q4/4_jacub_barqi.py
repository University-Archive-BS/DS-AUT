n, x = map(int, input().split())
stuff = input().split()

mid_sum_arr = []
mid_sum = 0
for i in range(n):
    if mid_sum + int(stuff[i]) > x:
        mid_sum_arr.append(int(mid_sum))
        mid_sum = int(stuff[i])
    else:
        mid_sum += int(stuff[i])
mid_sum_arr.append(int(mid_sum))
print(mid_sum_arr.__len__())
