def shortest(my_input):
    input_length = my_input.__len__()

    if input_length == 1 | isVarooKhaneh(my_input):
        return my_input

    begin = my_input[0]
    end = my_input[input_length - 1]

    if begin == end:
        return begin + shortest(my_input[1: input_length - 1]) + end

    else:
        same_head = shortest(my_input[1: input_length])
        varookhaneh1 = begin + same_head + begin
        hazineh1 = same_head.__len__() - (input_length - 1) + 2

        same_tail = shortest(my_input[0: input_length - 1])
        varookhaneh2 = end + same_tail + end
        hazineh2 = same_tail.__len__() - (input_length - 1) + 2

        if hazineh1 > hazineh2:
            return varookhaneh2

        if hazineh1 < hazineh2:
            return varookhaneh1

        if varookhaneh1.compareTo(varookhaneh2) < 0:
            return varookhaneh1
        else:
            return varookhaneh2


def isVarooKhaneh(my_input):
    input_length = my_input.__len__()
    left = 0
    right = (input_length - 1) - left

    while left <= right:
        if my_input[left] != my_input[right]:
            return False

        left += 1
        right -= 1

    return True


input_string = str(input())
print(shortest(input_string))
