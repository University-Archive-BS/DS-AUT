def calculate_j(ii):
    jj = ii + 1
    temp = 0
    while parentheses[jj] != ')':
        temp += 1
        jj += 1

    while temp != 0:
        jj += 1
        temp -= 1

    return jj


q = int(input())

parentheses = list(str(input()))
print(parentheses.__len__())
print(parentheses[0])

beautifully = [0 for k in range(q)]

i = 0
while i < q:
    if parentheses[i] == '(':
        j = i + 1
        while parentheses[j] != ')':
            j = calculate_j(j - 1)

        beautifully[i] = j - i
        i += j
    else:
        i += 1

print(max(beautifully))
