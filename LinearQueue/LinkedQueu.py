class Node:
    def __init__(self,value):
        self.value =  value
        self.next = None
class Queue:
    def __init__(self,size = 5):
        self.size = size
        self.front = None
        self.rear = None
        self.top = 0
    def insertion(self,value):
        if self.top < self.size:
            node = Node(value)
            if self.rear :
                self.rear.next = node
                self.rear = node
            else :
                self.rear = self.front = node
            self.top+=1
        else :
            print("Queue is full :")
    def deletion(self):
       if self.top ==0 :
           print("Queue is empty!")
       else :
           if self.rear == self.front :
               value = self.rear.value
               self.rear = self.front = None
           else :
               value = self.front.value
               self.front=self.front.next
           self.top-=1
           return value

    def __str__(self):  # for printing the linkedlist
        temp = self.front
        s = "Queue: "
        while temp:
            s = s + str(temp.value) + " "
            temp = temp.next
        return s
list = Queue()
print("Enter the operation you want to perform:")
print("Enter 1 to insertion")
print("Enter 2 to deletion")
print("Enter 3 to exit")
while True:
    option = int(input("Enter your choice:"))
    if option == 1:
        list.insertion(int(input("Enter the value you want to insertion:")))
    if option == 2:
        list.deletion()
    if option == 3:
        break
    print("\n", "    ", list)
