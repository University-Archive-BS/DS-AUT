def heap_sort(your_list):
    your_list = make_max_heap(your_list)
    elements = your_list.__len__()
    count = elements - 1
    while count >= 0:
        temp_oona = your_list[0]
        your_list[0] = your_list[count]
        your_list[count] = temp_oona
        count -= 1
        heapify(your_list, 0)
    return your_list


def make_max_heap(your_list):
    elements = your_list.__len__()
    tt = int(elements / 2)
    while tt > 0:
        heapify(your_list, tt)
        tt -= 1
    return your_list


def heapify(your_list, element):
    elements = your_list.__len__() - 1
    left = 2 * element
    right = 2 * element + 1

    max_ma = 0
    if left < elements and your_list[left] > your_list[element]:
        max_ma = left
    else:
        max_ma = element

    if right <= elements and your_list[right] > your_list[max_ma]:
        max_ma = right

    if max_ma != element:
        temp_ma = your_list[max_ma]
        your_list[max_ma] = your_list[element]
        your_list[element] = temp_ma
        heapify(your_list, max_ma)
    return your_list


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
            my_list = heap_sort(my_list)
            print(my_list)
    else:
        my_list.append(int(command[j].split(" ")[1]))
