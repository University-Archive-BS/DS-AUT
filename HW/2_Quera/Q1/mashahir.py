class Node:
    def __init__(self, value, father):
        self.value = value
        self.father = father
        self.leftChild = None
        self.rightChild = None

    def has_child(self):
        if self.leftChild or self.rightChild:
            return True
        else:
            return False

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None)
        else:
            self.insert_node(self.root, value)

        self.size += 1

    def insert_node(self, currentNode, value):
        if value <= currentNode.value:
            if currentNode.leftChild:
                self.insert_node(currentNode.leftChild, value)
            else:
                currentNode.leftChild = Node(value, currentNode)
        else:
            if currentNode.rightChild:
                self.insert_node(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value, currentNode)


n = int(input())
command = []

for i in range(n):
    command.append(input())

my_bst = BinarySearchTree()

for j in range(n):
    if command[j].__len__() == 1:
        if j < 3:
            print("No reviews yet")
        else:
            max_node = my_bst.root
            while max_node.has_child:
                max_node = max_node.rightChild

            result = max_node
            k = 1
            limit = int(my_bst.size / 3)
            while k < limit:
                if result
                k += 1
            print(result.value)


    else:
        my_bst.insert(int(command[j].split(" ")[1]))
