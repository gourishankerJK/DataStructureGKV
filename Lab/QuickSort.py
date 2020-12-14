def quicksort(l):
    n = len(l)
    def partition(l,low,high):
        pivot = l[low]
        i=low
        j = high
        while True :
            while True :
                i+=1
                if  i > len(l)-1 or l[i]>pivot :
                    break
            while True :
                j-=1
                if l[j]<=pivot:
                    break
            if i<j:
               l[i],l[j]=l[j],l[i]
            else :
               break
        l[low],l[j]=l[j],l[low]
        return j
    def _quicksort(l,low,high):
        if low<high:
            j=partition(l,low,high)
            _quicksort(l, low, j)
            _quicksort(l, j+1, high)
    _quicksort(l, 0, n)
    return l

print(quicksort(list(map(int,input("Enter the array separated by space: ").split()))))
