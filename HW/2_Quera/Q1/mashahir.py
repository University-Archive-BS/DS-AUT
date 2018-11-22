import heapq

n = int(input())
command = []

for i in range(n):
    command.append(input())

maxHeap = []
number_of_elements = 0

for j in range(n):
    if command[j].__len__() == 1:
        if j < 3:
            print("No reviews yet")
        else:
            temp = heapq.nlargest(int(number_of_elements / 3), maxHeap)
            print(temp[temp.__len__() - 1])
    else:
        heapq.heappush(maxHeap, int(command[j].split(" ")[1]))
        number_of_elements += 1
