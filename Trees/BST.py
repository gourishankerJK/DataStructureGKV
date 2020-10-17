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
                        temp.left = node
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = node
                        break
                    temp = temp.right

    def inorder(self):
        root = self.root
        print("Inorder :", end="")

        def inorderp(root):
            if root:
                inorderp(root.left)
                print(root.value, end=" ")
                inorderp(root.right)
        inorderp(root)
        print()

    def postorder(self):
        root = self.root
        print("Postorder :", end=" ")

        def postorderp(root):
            if root:
                postorderp(root.left)
                postorderp(root.right)
                print(root.value, end=" ")
        postorderp(root)
        print()

    def preorder(self):
        root = self.root
        print("Preorder :", end="")

        def preorderp(root):
            if root:
                print(root.value, end=" ")
                preorderp(root.left)
                preorderp(root.right)
        preorderp(root)
        print()

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
for i in range(-10, 100, 20):
    tree.insert(i)
tree.inorder()
tree.postorder()
tree.preorder()
tree.search(13)
