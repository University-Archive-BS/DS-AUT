from collections import defaultdict
from itertools import chain


def DFS(G, v, seen=None, path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths


n = int(input())

nodes = [[0 for x in range(2)] for y in range(n - 1)]

numbers = []
for i in range(n - 1):
    nodes[i][0], nodes[i][1] = map(str, input().split())
    if not nodes[i][0] in numbers:
        numbers.append(nodes[i][0])

    if not nodes[i][1] in numbers:
        numbers.append(nodes[i][1])

G = defaultdict(list)
for (s, t) in nodes:
    G[s].append(t)
    G[t].append(s)

all_paths = list(chain.from_iterable(DFS(G, n) for n in set(G)))
max_len = max(len(p) for p in all_paths)
max_paths = [p for p in all_paths if len(p) == max_len]

print(max_len - 1)
