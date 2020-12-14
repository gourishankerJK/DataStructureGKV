class Queue():
    def __init__(self, size=100):
        self.Max_size = size
        self.front = self.rear = -1
        self.arr = size * [None]

    def enqueue(self, value):
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

    def dequeue(self):
        if(self.front == -1):  # Queue Empty Conditon
            return
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
    def isempty(self):
        return self.front == -1
def BFS(g, start, n):
    i = start
    visited = [0 for _ in range(n)]
    queue = Queue(n)
    print(i)
    queue.enqueue(i)
    visited[i] = 1
    while not queue.isempty():
        i = queue.dequeue()
        for j in range(n):
            if g[i][j] == 1 and visited[j] == 0:
                print(j)
                visited[j] = 1
                queue.enqueue(j)


n = int(input("Enter the number of vertices : "))
print("""# Example of adjacency matrix :
   g = [[0, 1, 0, 1, 0, 0, 0],
#      [1, 0, 1, 1, 0, 0, 0],
#      [0, 1, 0, 0, 1, 0, 0],
#      [1, 1, 0, 0, 1, 0, 0],
#      [0, 0, 1, 1, 0, 1, 1],
#      [0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 1, 0, 0]]""")
g = []
for x in range(n):
    g.append([])
    for y in range(n):
        print("Enter the vertices for ",x,": " )
        g[x].append(int(input()))
BFS(g, int(input("Enter the staring vertice: ")), n)
