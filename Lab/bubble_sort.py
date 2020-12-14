def bubblesort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                l[j+1],l[j]=l[j],l[j+1]
    return l
print(bubblesort(list(map(int,input("Enter the array separated by space: ").split()))))
