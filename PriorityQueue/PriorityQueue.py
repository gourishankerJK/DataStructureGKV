class PriorityQueue():
    def __init__(self, size=5):
        self.Max_size = size
        self.front = -1
        self.rear = -1
        self.list = [[None for _ in range(5)] for _ in range(2)]

    def insert(self, value, priority):
        if self.rear == -1:
            self.front = 0
            self.rear = 0
            self.list[0][self.rear] = value
            self.list[1][self.rear] = priority
        elif self.rear == self.Max_size - 1:
            print("PriorityQueue is full")
        else:
            index = self.rear
            flag = 0
            while True:
                print(self.list[1][index], priority, value)
                if self.list[1][index] > priority and index != 0:
                    if index == self.rear:
                        self.rear += 1
                        self.list[1][self.rear] = self.list[1][index]
                        self.list[0][self.rear] = self.list[0][index]
                        flag = 1
                    index -= 1
                else:
                    break
            if flag != 1:
                self.rear += 1
                self.list[1][self.rear] = priority
                self.list[0][self.rear] = value

    def Del(self):
        if self.front == -1:
            print("Queue empty!")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            temp = 0
            while temp < self.front:
                self.list[0][temp] = self.list[0][temp + 1]
                temp += 1

    def __str__(self):
        s = "Queue :"
        for i in range(self.front, self.rear + 1):
            s += str(self.list[0][i])
        return s


l = PriorityQueue()
l.insert(1, 2)
l.insert(2, 2)
l.insert(3, 1)
print(l)
print(l.list)
l.Del()
print(l.list)
