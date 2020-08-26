from os import system, name
from time import sleep

# this function is created to clear the screen and it doesn't have to do anything with queue


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Queue():
    def __init__(self, size=5):
        self.Max_size = size
        self.front = self.rear = -1
        self.arr = size * [None]

    def insertion(self, value):
        if((self.rear - self.front == self.Max_size - 1) or (self.rear + 1 == self.front)):  # Queue Full condition similar to self.front == 0 and self.rear == Max_size -1 as this is same as  rear - front = size -1
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

    def deletion(self):
        if(self.front == -1):  # Queue Empty Conditon
            print("\nQueue is empty!")
        if self.front == self.rear:
            value = self.rear
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
            for i in range(0, self.rear+1):
                s += str(self.arr[i]) + " "
        return s


list = Queue()
while True:
    print("Enter the operation you want to perform:")
    print("Enter 1 to insertion")
    print("Enter 2 to deletion")
    print("Enter 3 to exit")
    option = int(input("Enter your choice:"))
    if option == 1:
        list.insertion(int(input("Enter the value you want to insertion:")))
    if option == 2:
        list.deletion()
    if option == 3:
        break
    print("\n", "    ", list)
    sleep(1.5)
    clear()
