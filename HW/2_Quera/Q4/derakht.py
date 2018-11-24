from collections import deque


class Graph:
    def __init__(self, v):
        self.v = v
        self.neighbors = [deque()] * v

    def add_neighbor(self, neighbor):
        self.neighbors.appendleft(neighbor)


n = int(input())

nodes = [[0 for x in range(2)] for y in range(n)]

numbers = []
for i in range(n):
    nodes[i][0], nodes[i][1] = map(int, input().split())
    if not nodes[i][0] in numbers:
        numbers.append(nodes[i][0])

    if not nodes[i][1] in numbers:
        numbers.append(nodes[i][1])

graph = Graph(5)
graphs = []

