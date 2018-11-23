class Node:
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(Node(value))

    def insert_node(self, new_node):
        traversal_node = self.root
        current_node = self.root
        while traversal_node:
            current_node = traversal_node
            if new_node.value < traversal_node.value:
                traversal_node.count += 1
                traversal_node = traversal_node.left
            else:
                traversal_node = traversal_node.right
        if new_node.value < current_node.value:
            current_node.left = new_node
        else:
            current_node.right = new_node

    def Kth_smallest(self, k):
        ret = -1
        traverse_node = self.root
        while traverse_node is not None:
            if traverse_node.count + 1 == k:
                ret = traverse_node.value
                break
            elif traverse_node.count < k:
                k = k - (traverse_node.count + 1)
                traverse_node = traverse_node.right
            else:
                traverse_node = traverse_node.left
        return ret


n = int(input())
command = []

numbers = 0
bst = BST()

for i in range(n):
    command.append(input())
    if command[i].__len__() == 1:
        if numbers < 3:
            print("No reviews yet")
        else:
            print(bst.Kth_smallest(numbers - int(numbers / 3) + 1))

    else:
        bst.insert(int(command[i].split(" ")[1]))
        numbers += 1