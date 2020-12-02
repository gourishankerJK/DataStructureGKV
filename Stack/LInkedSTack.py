class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,size = 5):
        self.size = size
        self.first = None
        self.last = None
        self.top= 0

    def length(self):    # returns the length at just o(1) ,i.e constant time
        return self.len

    def push(self, value):  # appends the element at the last
        if self.top < self.size :
            node = Node(value)
            if self.first == self.last == None:
                self.first = node
                self.last = node
            else:
                self.last.next = node
                self.last = node
            self.top += 1
        else :
            print("Stack Overflow!")
    def pop(self):   # deletes the last elements of linkedlist
        cur = self.first
        if self.top <= 0:
            print("STack underflow!")
            return
        if cur.next == None :
            self.last = self.first = None
            self.top -= 1
            return cur.value

        while cur.next != None:
            prev = cur
            cur = cur.next
        prev.next = None
        self.last = prev
        self.top -= 1
        return cur.value
    def __str__(self):  # for printing the linkedlist
        temp = self.first
        s = []
        string =""
        while temp:
            s.append(str(temp.value))
            temp = temp.next
        for i in s[::-1]:
            string += i+"\n"
        return string
list = Stack()
print("Enter the operation you want to perform:")
print("Enter 1 to insertion")
print("Enter 2 to deletion")
print("Enter 3 to exit")
while True:
    option = int(input("Enter your choice:"))
    if option == 1:
        list.push(int(input("Enter the value you want to insertion:")))
    if option == 2:
        list.pop()
    if option == 3:
        break
    print("\n", list)
