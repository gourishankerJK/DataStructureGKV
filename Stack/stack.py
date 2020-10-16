class Stack():
    MyName = "Gouri Shanker"
    def __init__(self, size=5):
        self.Max_size = size
        self.arr = size * [None]
        self.top = -1

    def push(self, value):
        if value %2 != 0:
            if self.top < self.Max_size - 1:
                self.top += 1
                self.arr[self.top] = value

            else:
                print()
                print("\nStack Overflow!")
        else :
            print("Invalid ,Enter odd value!")

    def pop(self):
        if self.top == -1:
            print("\nStack Underflow!")
        else:
            value = self.arr[self.top]
            self.top -= 1
            print("Pop Sucessful!\n")
            return value**2

    def __str__(self):
        length = self.top
        s = ""
        for i in range(length, -1, -1):
            s = s + str(self.arr[i]) + "\n"
        return s


list = Stack()
print("Enter the operation you want to perform:")
print("Enter 1 to push")
print("Enter 2 to pop")
print("Enter 3 to exit")
while True:
    option = int(input("Enter your choice:"))
    if option == 1:
        list.push(int(input("Enter the value you want to push:")))
        print()
        print(list)
        print()
    if option == 2:
        print(list.pop())
        print()
        print(list)
        print()
    if option == 3:
        break
