class Node :
    def __init__(self,value,power):
        self.next = None
        self.value = value
        self.power = power
class Polynomil:
    def __init__(self):
        self.first = None
        self.last = None
    def append(self, value,power):  # appends the element at the last
        node = Node(value,power)
        if self.first == self.last == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.len += 1
print("Enter the 1st Polynomial :")
firstdergree = int(input("Enter the dergree of 1st Polynomial:"))
cofficient = input("Enter the cofficient separated by space :").split()
for i in range(firstdergree,-1,-1):
    
print("Enter the 2st Polynomial :")
seconddergree = int(input("Enter the dergree of 2st Polynomial:"))
cofficients = input("Enter the cofficient separated by space :").split()
