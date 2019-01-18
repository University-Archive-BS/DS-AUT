def howMany(values):
    n = len(values)
    max_ = sum(values)
    values = list(values)
    values.sort()
    count = 0
    i = 0
    while i < n:
        G = 1
        while i + G < n and values[i + G] == values[i]:
            G += 1

        ways_below = [0] * (max_ + 1)
        ways_below[0] = 1
        for k in range(i):
            for s in range(max_, values[k] - 1, -1):
                ways_below[s] += ways_below[s - values[k]]

        for g in range(1, G + 1):

            ways_above = [0] * (max_ + 1)
            ways_above[0] = 1
            for k in range(i + g, n):
                for s in range(max_, values[k] - 1, -1):
                    ways_above[s] += ways_above[s - values[k]]

            for s in range(g * values[i], max_ + 1):
                count += nCr(G, g) * ways_below[s - g * values[i]] * ways_above[s]
        i += G
    return count

def howManyImproved(values):
    n = len(values)
    max_ = sum(values)
    values.sort()
    count = 0
    for i in range(n):
        ways_below = [0] * (max_ + 1)
        ways_below[0] = 1
        for k in range(i):
            for s in range(max_, values[k] - 1, -1):
                ways_below[s] += ways_below[s - values[k]]
        ways_above = [0] * (max_ + 1)
        ways_above[0] = 1
        for k in range(i + 1, n):
            for s in range(max_, values[k] - 1, -1):
                ways_above[s] += ways_above[s - values[k]]
        for s in range(values[i], max_ + 1):
            count += ways_below[s - values[i]] * ways_above[s]
    return count

def howManyInitial(values):
    n = len(values)
    x = sum(values)
    values.sort()
    non_zero = set()

    A = [[0] * (x + 1) for _ in range(n)]
    B = [[0] * (x + 1) for _ in range(n)]
    for i in range(1, 2 ** n):
        lsb = get_lsb(i)
        msb = get_msb(i)
        total = int_to_total(i, values)
        A[msb][total] += 1
        B[lsb][total] += 1
        non_zero.add(total)

    ways = 0
    for k in non_zero:
        for i in range(n - 1):
            for j in range(i + 1, n):
                ways += A[i][k] * B[j][k]
    return ways


def nCr(n, r):
    if r > n / 2:
        return nCr(n, n - r)
    if r == 0:
        return 1
    top = 1
    bottom = 1
    for i in range(r):
        top *= n - i
        bottom *= i + 1
    return top / bottom


def get_lsb(x):
    if not x:
        return -1
    i = 0
    while not x & 1 << i:
        i += 1
    return i


def get_msb(x):
    i = -1
    while x:
        x >>= 1
        i += 1
    return i


def int_to_total(x, values):
    return sum(values[i] for i in range(len(values)) if x & 1 << i)


if __name__ == '__main__':
    n = int(input())
    string = list(map(int, input().split()))
    print(int(howMany(string)))
