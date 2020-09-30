class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
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
            node.next = self.first
        else:
            self.last.next = node
            self.last = node
            node.next = self.first
        self.len += 1

    def prepend(self, value):  # inserts at the beginning
        node = Node(value)
        if self.first == self.last == None:
            self.first = node
            self.last = node
            node.next = self.first
        else:
            node.next = self.first
            self.first = node
            self.last.next = self.first
        self.len += 1

    def insert(self, value, pos):  # Inserts the element at given position
        node = Node(value)
        if pos > self.len + 1:
            raise "Position don't exist!"
            return
        elif pos == 1:
            self.prepend(value)
            return
        elif pos == self.len +1 :
            self.append(value)
            return
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
        while cur.next != self.first:
            prev = cur
            cur = cur.next
        prev.next = self.first
        self.last = prev
        self.last.next = self.first
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
            self.last.next = self.first
            return value
        count = 1
        while count < pos:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = cur.next
        value = cur.value
        cur.next = self.first
        return value
    def delvalue(self ,value):
        temp = self.first
        if temp == None :
            print("LL is empty!")
            return

        if temp.value == value :
            self.remove(1)
            return
        temp = temp.next
        count = 2
        while True :
            if temp.value == value :
                self.remove(count)

                return
            temp = temp.next
            if temp == self.first :
                break
            count +=1
        print("No such element is present!")
        return


    def __str__(self):
        temp = self.first
        s = "Circular Linkedlist :"
        if temp :
            while True:
                s = s + str(temp.value) + " "
                temp = temp.next
                if temp == self.first:
                    break
        return s
list = CircularLinkedList()
print("Welcome ,\nEnter \n1 for insertion at beginging \n2 to insert at last \n3 to insert by position \n4 to delete the value at beginggng \n5 To delete at last \n6 To delete at any given postion\n7 to delete by value\n8 to exit")
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
    elif int(input1) == 7 :
        list.delvalue(int(input('Enter the value :')))
    elif int(input1) == 8 :
        break
    else :
        print("Invalid input !")
    print(list)
