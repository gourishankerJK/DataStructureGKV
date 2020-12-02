class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.back = None


class DoubleLinkedList():
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, value):
        node = Node(value)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            node.back = self.last
            self.last.next = node
            self.last = node

    def prepend(self, value):
        node = Node(value)
        if self.first == None:
            self.first = node
            node.back = self.first
        else:
            node.next = self.first
            self.first.back = node
            self.first = node
    def insert(self,value,pos=1)

    def __str__(self):  # for printing the linkedlist
        temp = self.first
        s = "LinkedList: "
        while temp:
            s = s + str(temp.value) + " "
            temp = temp.next
        return s


list = DoubleLinkedList()
