class Node:
    def __init__(self, value, pr):
        self.data = value
        self.pr = pr
        self.next = None


class PriorityQueue:
    def __init__(self, size=5):
        self.size = size
        self.len = 0
        self.size = size
        self.head = None
        self.tail = None

    def insert(self, value, pro):
        if self.len <= self.size:
            self.len += 1
            node = Node(value, pro)
            if self.head is None:
                self.head = self.tail = node
            elif self.head.pr < node.pr:
                node.next = self.head
                self.head = node
            elif self.tail.pr > node.pr:
                self.tail.next = node
                self.tail = node

            else:
                cur = self.head.next
                prev = self.head
                while cur is not None:
                    if cur.pr == node.pr:
                        node.next = cur.next
                        cur.next = node
                        break
                    elif cur.pr < node.pr:
                        node.next = cur
                        prev.next = node
                        break
                    else:
                        prev = cur
                        cur = cur.next


        else:
            print("Queue is full!")

    def DEL(self):
        if self.head:
            value = self.head.data
            self.head = self.head.next
            return value
        else:
            print("PQ is empty!")

    def __str__(self):
        temp = self.head
        s = "PQ :"
        while temp:
            s = s + str(temp.data) + " "
            temp = temp.next
        return s


list = PriorityQueue(5)
print("Enter the operation you want to perform:")
print("Enter 1 to insertion")
print("Enter 2 to deletion")
print("Enter 3 to exit")
while True:
    option = int(input("Enter your choice:"))
    if option == 1:
        list.insert(int(input("Enter the value you want to insert: ")),int(input("\nEnter the priority of the element : ")))
    if option == 2:
        list.DEL()
    if option == 3:
        break
    print("\n", "    ", list)
