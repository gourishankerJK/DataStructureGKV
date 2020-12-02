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
        if cur.next == None :
            self.last = self.first = None
            self.len -= 1
            return cur.value
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
list = LinkedList()
print("Welcome ,\nEnter \n1 for insertion at beginging \n2 to insert at last \n3 to insert by position \n4 to delete the value at beginggng \n5 To delete at last \n6 To delete at any given postion\n8 to exit")
while True :
    input1 = input("Enter your choice :")
    if int(input1) == 1 :
        list.prepend(int(input('Enter the value :')))
    elif int(input1) == 2 :
        list.append(int(input('Enter the value :')))
    elif int(input1) ==  3:
        pos = int(input("Enter the postion :"))
        value = int(input("Enter the value"))
        list.insert(value,pos)
    elif int(input1) == 4 :
        list.remove()
    elif int(input1) == 5 :
        list.pop()
    elif int(input1) == 6 :
        list.remove(int(input('Enter the postion :')))
    elif int(input1) == 8 :
        break
    else :
        print("Invalid input !")
    print(list)
