class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(value, self.root)

    def insert_node(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._insert(value, node.right)
            else:
                node.right = Node(value)


n = int(input())
command = []

for i in range(n):
    command.append(input())

numbers = 0

bst = BST()

for j in range(n):
    if command[j].__len__() == 1:
        if j < 3:
            print("No reviews yet")
        else:
            print(kth_smallest(bst.root, numbers - int(numbers / 3)))

    else:
        bst.insert(int(command[j].split(" ")[1]))
        numbers += 1
