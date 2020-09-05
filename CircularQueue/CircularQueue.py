class Queue():
    def __init__(self, size=5):
        self.Max_size = size
        self.front = self.rear = -1
        self.arr = size * [None]

    def INSERT(self, value):
        if((self.rear == self.Max_size - 1 and self.front == 0) or (self.rear + 1 == self.front)):
            print("\nQueue is full")
        elif(self.rear == -1):
            self.rear = self.front = 0
            self.arr[self.rear] = value
        elif self.rear == self.Max_size - 1 and self.front > 0:
            self.rear = 0
            self.arr[self.rear] = value
        else:
            self.rear += 1
            self.arr[self.rear] = value

    def DEL(self):
        if(self.front == -1):  # Queue Empty Conditon
            print("\nQueue is empty!")
        if self.front == self.rear:
            value = self.arr[self.rear]
            self.front = self.rear = -1
            return value
        elif self.front == self.Max_size - 1 and self.rear >= 0:
            value = self.arr[self.front]
            self.front = 0
            return value

        else:
            value = self.arr[self.front]
            self.front += 1
            return value

    def __str__(self):
        s = "Queue : "
        if self.front < self.rear or self.front == self.rear and self.front != -1:
            for i in range(self.front, self.rear + 1):
                s += str(self.arr[i]) + " "
        elif self.front == -1:
            s = "\nQueue Empty!"
        else:
            for i in range(self.front, self.Max_size):
                s += str(self.arr[i]) + " "
            for i in range(0, self.rear + 1):
                s += str(self.arr[i]) + " "
        return s


list = Queue()
print("Enter the operation you want to perform:")
print("Enter 1 to INSERT")
print("Enter 2 to DELETE")
print("Enter 3 to exit")
print("Enter 4 to display")
while True:

    option = int(input("Enter your choice:"))
    if option == 1:
        list.INSERT(int(input("Enter the value you want to INSERT:")))
    elif option == 2:
        list.DEL()
    elif option == 3:
        break
    elif option == 4:
        print(list)
    else:
        print("Invaild input :(")

    print("\n", "    ", list)
