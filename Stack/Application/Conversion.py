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
            # print()
            # print("\nStack Overflow!")
            pass

    def pop(self):
        if self.top == -1:
            # print("\nStack Underflow!")
            return
        else:
            value = self.arr[self.top]
            self.top -= 1
            return value


def Postfix(exp):
    list = Stack(len(exp))
    s = ""
    for i in exp:
        if i in ["*", "+", "-", "/", "(", "[", "{"]:
            list.push(i)
        else:
            if i in ")}]":
                while list.top != -1:
                    sign = list.pop()
                    if sign in "[({":
                        break
                    elif sign not in ["(", "[", "{"]:
                        s += str(sign)
            else:
                s += str(i)
    while list.top != -1:
        sign = str(list.pop())
        if sign not in ["(", "[", "{"]:
            s += sign
    return s


def reverse(exp):
    reversed_exp = ""
    for i in exp[::-1]:
        if i in ")]}":
            reversed_exp += "("
        elif i in "[({":
            reversed_exp += ")"
        else:
            reversed_exp += str(i)
    return reversed_exp


def Prefix(exp):
    return reverse(Postfix(reverse(exp)))


expression = input("Enter the expression :")
print("Prefix :", Prefix(expression))
print("Postfix :", Postfix(expression))
