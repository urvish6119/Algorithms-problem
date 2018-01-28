# Binary Search is only useful on ordered list.
def binary_search(list1, ele):
    if len(list1) == 0:
        return False
    else:
        mid = len(list1) / 2
        if list1[mid] == ele:
            return True
        else:
            if ele < list1[mid]:
                return binary_search(list1[:mid], ele)
            else:
                return binary_search(list1[mid + 1:], ele)
print('enter array elements here with space')
list_i = [int(a) for a in input().split()]
search = int(input('please enter number you want to find.'))
binary_search(list_i, search)
