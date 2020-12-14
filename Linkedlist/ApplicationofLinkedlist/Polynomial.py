class Node:
    def __init__(self, value, power):
        self.next = None
        self.value = value
        self.power = power


class Polynomil:
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, value, power):  # appends the element at the last
        node = Node(value, power)
        if self.first == self.last == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def polyadd(self, p1, p2):
        temp1 = p1.first
        temp2 = p2.first
        while temp1 is not None and temp2 is not None:
            if temp1.power > temp2.power:
                self.append(temp1.value, temp1.power)
                temp1 = temp1.next
            elif temp2.power > temp1.power:
                self.append(temp2.value, temp2.power)
                temp2 = temp2.next
            else:
                self.append(temp2.value + temp1.value, temp2.power)
                temp1 = temp1.next
                temp2 = temp2.next
        if temp1 is None:
            while temp2 is not None:
                self.append(temp2.value, temp2.power)
                temp2 = temp2.next
        if temp2 is None:
            while temp1 is not None:
                self.append(temp1.value, temp1.power)
                temp1 = temp1.next

    def __str__(self):
        temp = self.first
        s = ""
        while temp.next is not None:
            s += str(temp.value) + "x^" + str(temp.power) + " + "
            temp = temp.next
        s += str(temp.value) + "x^" + str(temp.power) + "  "
        return s


poly1 = Polynomil()
poly2 = Polynomil()
result_poly = Polynomil()
print("Please Enter the exponents in decreasing order!!\n")
n=int(input("Enter the number of terms in first polynomial: "))
for _ in range(n):
    poly1.append(int(input("Enter the cofficient: ")),int(input("Enter the exponent: ")))
print("Poly :",poly1)
n=int(input("Enter the number of terms in second polynomial: "))
for _ in range(n):
    poly2.append(int(input("Enter the cofficient: ")),int(input("Enter the exponent: ")))
print("Poly",poly2)
result_poly.polyadd(poly1,poly2)
print("  ",poly1,"\n","+\n","  ",poly2,"\n-----------------------------------------\n",result_poly)
