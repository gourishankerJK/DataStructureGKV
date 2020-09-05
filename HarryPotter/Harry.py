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
            return "$"
        if self.front == self.rear:
            value = self.arr[self.front]
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


class Stack():
    def __init__(self, size=5):
        self.Max_size = size
        self.arr = size * [None]
        self.top = -1

    def push(self, value):
        if self.top < self.Max_size - 1:
            self.top += 1
            self.arr[self.top] = value

        else:
            print()
            # print("\nStack Overflow!")

    def pop(self):
        if self.top == -1:
            return "$"
        else:
            value = self.arr[self.top]
            self.top -= 1
            # print("Pop Sucessful!\n")
            return value


Dumbledore = [0, 0]
n = int(input("Size of army : "))
Harry = Stack(n)
Voldemort = Queue(n)
for i in range(n):
    s = int(input("Enter the soldiers power in numbers :"))
    Harry.push(s)
    Voldemort.INSERT(s)
while True:
    Voldemort_army = Voldemort.DEL()
    harry_army = Harry.pop()
    if harry_army == "$" or Voldemort_army == "$":
        break
    elif harry_army > Voldemort_army:
        Dumbledore[0] += 1
    elif harry_army < Voldemort_army:
        Dumbledore[1] += 1
if Dumbledore[0] > Dumbledore[1]:
    print("Harry Wins by {} / {} ".format(Dumbledore[0], Dumbledore[1]))
elif Dumbledore[0] < Dumbledore[1]:
    print("Voldemort Wins {} / {} ".format(Dumbledore[1], Dumbledore[0]))
else:
    print("Draw by  {} , {} ".format(Dumbledore[0], Dumbledore[1]))
