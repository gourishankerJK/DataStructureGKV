class Avltree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None
            self.height = 1

    def __init__(self):
        self.__root = None

    def __Nodeheight(self, node):
        hl = node.left.height if node and node.left else 0
        hr = node.right.height if node and node.right else 0
        return hl + 1 if hl > hr else hr + 1

    def __Balancefactor(self, node):
        hl = node.left.height if node and node.left else 0
        hr = node.right.height if node and node.right else 0
        return hl - hr

    def __parent(self, node):
        temp = self.__root
        while temp.value != node.value:
            parent = temp
            if temp.value < node.value:
                temp = temp.right
            else:
                temp = temp.left
        return parent

    def __LLrotation(self, node):
        nodeleft = node.left
        noderight = nodeleft.right
        nodeleft.right = node
        node.left = noderight
        node.height = self.__Nodeheight(node)
        nodeleft.height = self.__Nodeheight(nodeleft)
        if self.__root == node:
            self.__root = nodeleft
        else:
            parentnode = self.__parent(node)
            if parentnode.left == node:
                parentnode.left = nodeleft
            else:
                parentnode.right = nodeleft
        return nodeleft

    def __LRrotation(self, node):
        nodeleft = node.left
        noderight = nodeleft.right
        nodeleft.right = noderight.left
        node.left = noderight.right
        noderight.left = nodeleft
        noderight.right = node
        node.height = self.__Nodeheight(node)
        nodeleft.height = self.__Nodeheight(nodeleft)
        noderight.height = self.__Nodeheight(noderight)
        if self.__root == node:
            self.__root = noderight
        else:
            parentnode = self.__parent(node)
            if parentnode.left == node:
                parentnode.left = noderight
            else:
                parentnode.right = noderight
        return noderight

    def __RRrotation(self, node):
        nodeleft = node.right
        noderight = nodeleft.left
        nodeleft.left = node
        node.right = noderight
        node.height = self.__Nodeheight(node)
        nodeleft.height = self.__Nodeheight(nodeleft)
        if self.__root == node:
            self.__root = nodeleft
        else:
            parentnode = self.__parent(node)
            if parentnode.left == node:
                parentnode.left = nodeleft
            else:
                parentnode.right = nodeleft
        return nodeleft

    def __RLrotation(self, node):
        nodeleft = node.right
        noderight = nodeleft.left
        nodeleft.left = noderight.right
        node.right = noderight.left
        noderight.right = nodeleft
        noderight.left = node
        node.height = self.__Nodeheight(node)
        nodeleft.height = self.__Nodeheight(nodeleft)
        noderight.height = self.__Nodeheight(noderight)
        if self.__root == node:
            self.__root = noderight
        else:
            parentnode = self.__parent(node)
            if parentnode.left == node:
                parentnode.left = noderight
            else:
                parentnode.right = noderight
        return noderight

    def __insert(self, node, value):
        if value < node.value:
            if node.left:
                self.__insert(node.left, value)
            else:
                node.left = self.Node(value)
        else:
            if node.right:
                self.__insert(node.right, value)
            else:
                node.right = self.Node(value)
        node.height = self.__Nodeheight(node)
        if self.__Balancefactor(node) == 2 and self.__Balancefactor(node.left) == 1:
            return self.__LLrotation(node)
        if self.__Balancefactor(node) == 2 and self.__Balancefactor(node.left) == -1:
            return self.__LRrotation(node)
        if self.__Balancefactor(node) == -2 and self.__Balancefactor(node.right) == -1:
            return self.__RRrotation(node)
        if self.__Balancefactor(node) == -2 and self.__Balancefactor(node.right) == 1:
            return self.__RLrotation(node)

    def insert(self, value):
        if self.__root is None:
            self.__root = self.Node(value)
        else:
            print(self.__root.height)
            self.__insert(self.__root, value)

    def inorder(self):
        root = self.__root
        print("Inorder :", end="")

        def inorderp(root):
            if root:
                inorderp(root.left)
                print(root.value, end=" ")
                inorderp(root.right)
        inorderp(root)
        print()

    def postorder(self):
        root = self.__root
        print("Postorder :", end=" ")

        def postorderp(root):
            if root:
                postorderp(root.left)
                postorderp(root.right)
                print(root.value, end=" ")
        postorderp(root)
        print()


l = Avltree()
l.insert(30)
l.insert(20)
l.insert(40)
l.insert(85)
l.insert(40)
l.insert(15)
l.insert(97)
l.insert(37)
l.postorder()
l.inorder()
