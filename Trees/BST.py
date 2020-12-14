class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insertion(self,value):
        def _insert(root,node):
            if root.value < node.value :
                if root.right is not None :
                    _insert(root.right, node)
                else :
                    root.right = node
            else :
                if root.left is not None :
                    _insert(root.left, node)
                else :
                    root.left = node
        if self.root is None :
            self.root = self.Node(value)
        else :
            _insert(self.root,self.Node(value))

    def search(self, node, value, parent):
        if node:
            if node.value == value:
                return node, parent
        else:
            return None, None
        if node.value < value:
            return self.search(node.right, value, node)
        else:
            return self.search(node.left, value, node)

    def __isleaf(self, node):
        return node.left == node.right == None

    def __delleaf(self, node, parent):
        if node == parent.left:
            parent.left = None
        else:
            parent.right = None

    def __maximumnodefromleft(self, node):
        parent = node
        node = node.left
        while node.right is not None:
            parent = node
            node = node.right
        return node, parent

    def __minimumnodefromright(self, node):
        parent = node
        node = node.right
        while node.left is not None:
            parent = node
            node = node.left
        return node, parent

    def delete(self, value):
        if self.root is None :
            print("Tree is Empty!")
            return
        node, parent = self.search(self.root, value, self.root)
        if node is None and parent is None:
            print("Entered value not found!")
            return
        if self.__isleaf(node):
            self.__delleaf(node, parent)
        else:
            if node.left:
                new_node, parent = self.__maximumnodefromleft(node)
                node.value = new_node.value
            else:
                new_node, parent = self.__minimumnodefromright(node)
                node.value = new_node.value
            self.__delleaf(node, parent)
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
        tree.insertion(int(input("Enter the number you want to insert : ")))
        print()
    elif input1 == 2:
        tree.delete(int(input("Enter the you wanna delete :")))
        print()
    elif input1 == 3:
        tree.postorder()
        tree.inorder()
        tree.preorder()
    elif input1 == 4:
        break
    else:
        print("Invalid Key !")
