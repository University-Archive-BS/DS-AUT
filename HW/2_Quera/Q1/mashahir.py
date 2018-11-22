import heapq

n = int(input())
command = []

for i in range(n):
    command.append(input())

my_heap = []

for j in range(n):
    if command[j].__len__() == 1:
        if j < 3:
            print("No reviews yet")
        else:
            heapq.heapify(my_heap)
            large_ha = heapq.nlargest(int(my_heap.__len__() / 3), my_heap)
            print(large_ha[large_ha.__len__() - 1])
    else:
        my_heap.append(int(command[j].split(" ")[1]))

