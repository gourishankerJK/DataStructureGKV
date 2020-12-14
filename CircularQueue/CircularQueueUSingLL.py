class Node:
    def __init__(self):
        self.data = None
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enQueue(q, value):
        temp = Node()
        temp.data = value
        if (q.front == None):
            q.front = temp
        else:
            q.rear.link = temp

        q.rear = temp
        q.rear.link = q.front


    def deQueue(q):
        if (q.front == None):
            print("Queue is empty")
            return -999999999999


        value = None
        if (q.front == q.rear):
            value = q.front.data
            q.front = None
            q.rear = None
        else:
            temp = q.front
            value = temp.data
            q.front = q.front.link
            q.rear.link = q.front

        return value

    def __str__(q):
        temp = q.front
        s = "Elements in Circular Queue are: "
        if temp :
            while (temp.link != q.front):
                s+=str(temp.data)+" "
                temp = temp.link
            s+=str(temp.data)
        return s
list = Queue()
print("Enter the operation you want to perform:")
print("Enter 1 to insertion")
print("Enter 2 to deletion")
print("Enter 3 to exit")
while True:
    option = int(input("Enter your choice:"))
    if option == 1:
        list.enQueue(int(input("Enter the value you want to insertion:")))
    if option == 2:
        list.deQueue()
    if option == 3:
        break
    print("\n", "    ", list)
