class Node:
    def __init__(self):
        self.data = None
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    def enQueue(self, value):
        temp = Node()
        temp.data = value
        if (self.front == None):
            self.front = temp
        else:
            self.rear.link = temp

        self.rear = temp
        self.rear.link = self.front
        self.length+=1

    def deQueue(self):
        if (self.front == None):
            print("Queue is empty")
            return
        value = None
        if (self.front == self.rear):
            value = self.front.data
            self.front = None
            self.rear = None
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.link
            self.rear.link = self.front
        self.length-=1
        return value
    def __str__(self):
        temp = self.front
        s = "Queue: "
        while (temp.link != self.front):
            s +=str(temp.data)+" "
            temp = temp.link
        s+=str(temp.data)
        return s
list = Queue()
for i in range(10):
    list.enQueue(i)
    print(list)
for _ in range(5):
    list.deQueue()
    print(list)
list.enQueue(5)
print(list)
