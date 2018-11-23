class Node:
    def __init__(self):
        self.value = 0
        self.count = 0
        self.right = None
        self.left = None

    def set_value(self, value):
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = root

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
        while traverse_node:
            if traverse_node.count == (k - 1):
                ret = traverse_node.value
            elif traverse_node.value < k:
                k = k - (traverse_node.count + 1)
                traverse_node = traverse_node.right
            else:
                traverse_node = traverse_node.left
        return ret


n = int(input())
command = []

for i in range(n):
    command.append(input())

numbers = 0

bst = BinarySearchTree()

for j in range(n):
    if command[j].__len__() == 1:
        if j < 3:
            print("No reviews yet")
        else:
            print(bst.root.left.value)
            # for t in range(numbers):
            #     print(bst.Kth_smallest(t))
            # print(bst.Kth_smallest(numbers - int(numbers / 3)))

    else:
        temp_man = Node()
        temp_man.set_value(int(command[j].split(" ")[1]))
        if numbers == 0:
            bst.set_root(temp_man)
        else:
            bst.insert_node(temp_man)
        numbers += 1

