class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        temp = self.root
        if temp is None:
            self.root = node
        else:
            while True:
                if temp.value > value:
                    if temp.left is None:
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        break
                    temp = temp.right
            if temp.value > value:
                temp.left = node
            else:
                temp.right = node

    def search(self, value):
        temp = self.root
        flag = 0
        if temp is None:
            print("Tree is Empty!")
        else:
            while temp is not None:
                if temp.value == value:
                    flag = 1
                    break
                elif temp.value < value:
                    temp = temp.right
                else:
                    temp = temp.left
            if flag == 1:
                print("Value found in the tree")
            else:
                print("Value not found in the tree")


tree = BinarySearchTree()
tree.insert(47)
for i in range(0, 70, 5):
    tree.insert(i)
for i in range(0,70):
    tree.search(i)
