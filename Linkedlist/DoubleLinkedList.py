class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


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
            node.prev = self.last
            self.last.next = node
            self.last = node

    def prepend(self, value):
        node = Node(value)
        if self.first == None:
            self.first = node
            node.prev = self.first
        else:
            node.next = self.first
            self.first.prev = node
            self.first = node

    def __str__(self):  # for printing the linkedlist
        temp = self.first
        s = "LinkedList: "
        while temp:
            s = s + str(temp.value) + " "
            temp = temp.next
        return s


list = DoubleLinkedList()
list.append(9)
list.append(10)
list.prepend(50)
print(list)
