# Binary Search is only useful on ordered list.
def binary_search(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) / 2
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return binary_search(arr[:mid], ele)
            else:
                return binary_search(arr[mid + 1:], ele)
print('enter array elements here with space')
list1 = [int(a) for a in input().split()]
search = int(input('please enter number you want to find.'))
binary_search(list1, search)