class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def length(self):    # returns the length at just o(1) ,i.e constant time
        return self.len

    def append(self, value):  # appends the element at the last
        node = Node(value)
        if self.first == self.last == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.len += 1

    def prepend(self, value):  # inserts at the beginning
        node = Node(value)
        if self.first == self.last == None:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.len += 1

    def insert(self, value, pos):  # Inserts the element at given position
        node = Node(value)
        if pos > self.len + 1:
            raise "Position don't exist!"
            return
        elif pos == 0:
            self.prepend(value)
            return
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

    def pop(self):   # deletes the last elements of linkedlist
        cur = self.first
        while cur.next != None:
            prev = cur
            cur = cur.next
        prev.next = None
        self.last = prev
        self.len -= 1
        return cur.value


    def remove(self, pos=1):  # delete the at given position but by default deletes at the beginning position
        if self.len == 0:
            raise "Linkedlist is empty !"
        if self.len < pos or pos <= 0:
            raise "Invalid Position!"
        if self.len == pos != 1:
            return self.pop()
        cur = self.first
        self.len -= 1
        if pos == 1  and self.first.next == self.first :
            value = self.first.value
            self.first = None
            self.last = None
            return value
        if pos == 1:
            value = cur.value
            self.first = cur.next
            cur.next = None
            return value
        count = 1
        while count < pos:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = cur.next
        value = cur.value
        cur.next = None
        return value
    def __str__(self):  # for printing the linkedlist
        temp = self.first
        s = "LinkedList :"
        while temp:
            s = s + str(temp.value) + " "
            temp = temp.next
        return s
