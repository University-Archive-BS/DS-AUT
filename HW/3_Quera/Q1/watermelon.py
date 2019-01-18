def chandTa(values):
    # int[] values
    # Arrays.sort(values);

    number = values.__len__()

    fk = [0 for x in range(number)]
    for i in range(0, number):
        if i > 0 and values[i] == values[i - 1]:
            fk[i] = fk[i - 1] + 1
        else:
            fk[i] = 1

    gk = [0 for y in range(number)]
    for i in range(n - 1, -1, -1):
        if i < number - 1 and values[i] == values[i + 1]:
            gk[i] =  gk[i + 1] + 1
        else:
            gk[i] = 1

    mc = [0 for xx in range(number)]
    for i in range(0, number):
        for j in range(0, number):
            if values[i] == values[j]:
                mc[i] += 1

    # long[][] ch = new long[31][62];
    ch = [[0 for xxx in range(62)] for yyy in range(31)]
    for j in range(0, 61):
        ch[0][j] = 1
        for i in range(1, min(j, 30)):
            if i < j:
                ch[i][j] = ch[i][j - 1]

            ch[i][j] += ch[i - 1][j - 1]


    # f = new long[30001][30];
    f = [[0 for xxxx in range(30)] for yyyy in range(30001)]
    for k in range(1, 30001):
        for i in range(0, n):
            v = k - values[i] * fk[i];
            if v == 0:
                f[k][i] = 1

            elif v > 0:
                for j in range(0, i - fk[i] + 1):
                    f[k][i] += f[v][j] * ch[fk[j]][mc[j]]


    # long[][] g = new long[30001][30];
    g = [[0 for xxxxx in range(30)] for yyyyy in range(30001)]
    for k in range(1, 30001):
        for i in range(number - 1, 0, -1):
            v = k - values[i] * gk[i]
            if v == 0:
                g[k][i] = 1

            elif v > 0:
                for j in range(i + gk[i], number):
                    g[k][i] += g[v][j] * ch[gk[j]][mc[j]]

    tot = 0
    for i in range(1, 30001):
        for j in range(0, n - 1):
            for k in range(j + 1, n):
                a = fk[j]
                b = gk[k]
                c = mc[j]
                d = mc[k]
                t = f[i][j] * g[i][k]

                if t == 0:
                    continue

                if values[j] == values[k]:
                    t *= ch[a][c] * ch[b][c - a]

                else:
                    t *= ch[a][c] * ch[b][d]

                tot += t
    return tot


n = int(input())
string = list(map(int, input().split()))
print(int(chandTa(string)))
