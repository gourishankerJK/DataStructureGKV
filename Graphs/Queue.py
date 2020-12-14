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
        self.rear = -1
        self.front = 0
        self.arr = size * [None]

    def insertion(self, value):
        if(self.rear == self.Max_size - 1):
            print("Queue is full!")
        else:
            self.rear += 1
            self.arr[self.rear] = value

    def deletion(self):
        if(self.front > self.rear):
            print("Queue is empty!")
        else:
            value = self.arr[self.front]
            self.front += 1
            return value

    def __str__(self):
        s = "Queue : "
        if self.front < self.rear or self.front == self.rear and self.front != -1:
            for i in range(self.front, self.rear + 1):
                s += str(self.arr[i]) + " "
        elif self.rear == -1:
            s = "\nQueue Empty!"
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
