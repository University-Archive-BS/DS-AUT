# n, m, k = map(int, input().split())
#
# input_table = []
#
# for i in range(n):
#     input_table.append(input())
#
# print("Impossible")
#


class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.time = 0


vis = [[0 for x in range(110)] for y in range(110)]
vis1 = [[0 for x in range(110)] for y in range(110)]
time = [[0 for x in range(110)] for y in range(110)]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
my_map = [[" " for x in range(110)] for y in range(110)]

n, m, k = map(int, input().split())

out_queue = []

def check(x, y):
