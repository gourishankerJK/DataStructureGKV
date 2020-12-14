class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def insertion(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = self.Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = self.Node(value)

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


l = Tree()
l.insertion(50)
l.insertion(40)
l.insertion(60)
l.insertion(30)
l.insertion(45)
l.insertion(55)
l.insertion(70)
l.preorder()
l.postorder()
l.inorder()
l.delete(55)
l.delete(50)
l.preorder()
l.postorder()
l.inorder()
