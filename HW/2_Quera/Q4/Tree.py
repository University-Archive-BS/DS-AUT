class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    def __init__(self, size):
        self.vertices = size * [None]

    def insert_to_graph(self, v, u):
        if self.vertices[v] is None:
            self.vertices[v] = Vertex(u)
        else:
            temp = self.vertices[v]
            while temp.next is not None:
                temp = temp.next
            temp.next = Vertex(u)

    def print_graph(self):
        for vertex in self.vertices:
            j = vertex
            while j is not None:
                print(j.value)
                j = j.next

    def BFS(self, v):
        visited = len(self.vertices) * [False]
        queue = []
        distance = len(self.vertices) * [-1]
        visited[v] = True
        queue.append(v)
        u = None
        distance[v] = 0
        maximum = 0
        while len(queue) is not 0:
            u = queue.pop()
            element = self.vertices[u]
            while element is not None:
                if visited[element.value] is False:
                    visited[element.value] = True
                    queue.append(element.value)
                    distance[element.value] = distance[u] + 1
                element = element.next

        for i in range(len(self.vertices)):
            if distance[i] > maximum:
                maximum = distance[i]
                u = i
        return [u, maximum]


        # def bfs(self, u):
        #     dis = [-1] * self._vertices
        #     q = list()
        #     q.append(u)
        #     dis[u] = 0
        #     while not len(q) == 0:
        #         temp = q.pop()
        #         for i in self.edge:
        #             if dis[i] == -1:


        # def longest_path_length(self):
        #     first_tree = self.bfs(0)
        #     second_tree = self.bfs(first_tree.first)
        #     print(second_tree.second)


n = int(input())
graph = Graph(n)
for i in range(n - 1):
    edges = list(map(int, input().split(" ")))
    graph.insert_to_graph(edges[0] - 1, edges[1] - 1)
    graph.insert_to_graph(edges[1] - 1, edges[0] - 1)

print(graph.BFS(graph.BFS(0)[0])[1])
