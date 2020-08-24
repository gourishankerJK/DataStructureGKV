class Stack():
    def __init__(self, size=10):
        self.Max_size = size
        self.arr = size * [None]
        self.top = 0

    def push(self, value):
        if self.top < self.Max_size - 1:
            self.arr[self.top] = value
            self.top += 1
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            value = self.arr[self.top]
            self.top -= 1
            return value

    def __str__(self):
        length = self.top
        s = ""
        for i in range(length - 1, -1, -1):
            s = s + str(self.arr[i]) + "\n"
        if s == "":
            return "Stack is Empty!"
        return s
list = Stack(100)
for i in range(99):
    list.push(i)

print(list)

for _ in range(100):
    list.pop()
print(list)
