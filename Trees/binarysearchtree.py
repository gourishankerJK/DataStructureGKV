class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


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
                        node.parent = temp
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = node
                        node.parent = temp
                        break
                    temp = temp.right

    def deletion(self, value):
            def minvaluenode(node):
                current = node
                while current.left is not None :
                    current = current.left
                return current
            def d(root,value):
                if root is None :
                    return root
                if value < root.value :
                    root.left = d(root.left,value)
                elif value > root.value :
                    root.right = d(root.right,value)
                else :
                    if root.left is None :
                        temp = root.right
                        root = None
                        return temp
                    elif root.right is None :
                        temp = root.left
                        root = None
                        return temp
                    temp = minvaluenode(root.right)
                    root.value = temp.value
                    root.right = d(root.right,temp.value)
            return d(self.root,value)


    def inorder(self):
            root = self.root
            li=[]
            print("Inorder :", end="")

            def inorderp(root):
                if root:
                    inorderp(root.left)
                    li.append(root.value)
                    print(root.value, end=" ")
                    inorderp(root.right)
            inorderp(root)
            print()
            return li

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
            preo = []
            root = self.root
            print("Preorder :", end="")

            def preorderp(root):
                if root:
                    preo.append(root.value)
                    print(root.value, end=" ")
                    preorderp(root.left)
                    preorderp(root.right)
            preorderp(root)
            print()
            return preo


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
l= []
print("Enter the operations you want to perform :\n1 ,for insertion\n2,for deletion\n3,for printing tree in postorder\n4, in inorder\n5,in preorder \n 6 to exit \n  ")
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
    elif input1 == 4:
       ino = tree.inorder()
    elif input1 == 5:
       pro = tree.preorder()
    elif input1 == 6:
        break
    else:
        print("Invalid Key !")
