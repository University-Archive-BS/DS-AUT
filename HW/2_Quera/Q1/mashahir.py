import heapq

n = int(input())
command = []

for i in range(n):
    command.append(input())

my_list = []

for j in range(n):
    if command[j].__len__() == 1:
        if j < 3:
            print("No reviews yet")
        else:
            res = heapq.nlargest(int(my_list.__len__() / 3),  my_list)
            print(res[res.__len__() - 1])

    else:
        heapq.heappush(my_list, int(command[j].split(" ")[1]))
