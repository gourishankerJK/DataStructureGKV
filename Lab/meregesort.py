def mergesort(l):
    def _mergesort(l,low,mid,high):
        if low < high :
            mergesort(l,low,(low+high)//2)
            mergesort(l,(low+high)//2+1,high)
            merge()
