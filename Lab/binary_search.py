# def binarysearch(l,key):
#     low = 0
#     high = len(l)-1
#
#     def _binarysearch(l,key,low,mid,high):
#         mid = (high+low)//2
#         if low> high :
#             print("Value not found:")
#             return
#         if l[mid] == key :
#             print("VAlue found!")
#             return key
#         if l[mid]>key:
#             _binarysearch(l, key, low, mid, mid-1)
#         elif l[mid]< key:
#             _binarysearch(l, key, mid+1, mid, high)
#     _binarysearch(l,key,low,0,high)
# binarysearch(list(map(int,input("Enter the sorted array separated by space: ").split())), int(input("Enter the key: ")))
def selection_search(l,key):
    for i in l:
        if i == key :
            print("Found")
            return key
    print("Not found!")
selection_search(list(map(int,input("Enter the sorted array separated by space: ").split())), int(input("Enter the key: ")))
