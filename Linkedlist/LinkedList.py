class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def append(self, value):
        node = Node(value)
        if self.first == self.last == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.len += 1

    def prepend(self, value):
        node = Node(value)
        if self.first == self.last == None:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.len += 1

    def insert(self, value, pos):
        node = Node(value)
        if pos > self.len + 1:
            raise "Position don't exist!"
            return
        elif pos == 0:
            self.prepend(value)
        elif pos == self.len + 1:
            self.last.next = node
            self.last = node
        else:
            count = 0
            temp = self.first
            while (count < pos - 2):
                temp = temp.next
                count += 1
            node.next = temp.next
            temp.next = node
        self.len += 1

    def __str__(self):
        temp = self.first
        s = "LinkedList :"
        while temp:
            s = s + str(temp.value) + " "
            temp = temp.next
        return s


list = LinkedList()
for i in range(0, 50, 5):
    list.append(i)
print(list)
list.prepend(99)
print(list)
list.insert(22, 0)
print(list)
