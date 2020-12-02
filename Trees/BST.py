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
                if temp.value == value:
                    print("Redundant values are not allowed!")
                    break
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

    def deletion(self, value):
        def maxvaluenode(node, temp):
            current = node
            while current.right is not None:
                temp = current
                current = current.right
            return current, temp

        def minvaluenode(node, temp):
            current = node
            if current is None:
                current = temp.left.right
            while current.left is not None:
                temp = current
                current = current.left
            return current, temp

        def ischild(current):
            return (current.left is None and current.right is None)

        def d(current, value, temp, flag):
            while current is not None and current.value != value:
                temp = current
                if current.value > value:
                    current = current.left
                else:
                    current = current.right
            if current is None:
                if flag == 1:
                    return
                else:
                    print("VAlue not found!")
                    return
            if ischild(current):
                if temp.left is current:
                    temp.left = None
                else:
                    temp.right = None
                return
            return current

        if self.root is None:
            print("Tree is empty!")
            return
        current = self.root
        if current.value == value and current.left is None and current.right is None:
            self.root = None
            return

        flag = 0
        current = d(current, value, None, flag)
        if current is None:
            return
        flag = 1
        while not ischild(current):
            temp = current
            if current.right is not None:
                min_value, temp = minvaluenode(current.right, temp)
            else:
                min_value, temp = maxvaluenode(current.left, temp)
            current.value = min_value.value
            current = d(min_value, current.value, temp, flag)
            if current is None:
                break

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
                return True
            else:
                print("Value not found in the tree")
                return False


tree = BinarySearchTree()
print("Enter the operations you want to perform :\n1 ,for insertion\n2,for deletion\n3,for printing tree  \n4 to exit \n  ")
while True:
    input1 = int(input("Enter the number: "))
    if input1 == 1:
        tree.insert(int(input("Enter the number you want to insert : ")))
        print()
    elif input1 == 2:
        tree.deletion(int(input("Enter the you wanna delete :")))
        print()
    elif input1 == 3:
        tree.postorder()
        tree.inorder()
        tree.preorder()
    elif input1 == 4:
        break
    else:
        print("Invalid Key !")
