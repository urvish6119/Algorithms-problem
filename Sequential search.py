# Unordered list:
def sequential_search(array, element):
    position = 0
    found = False
    while position < len(array) and not found:
        if array[position] == element:
            found = True
        else:
            position += 1
    print(found)
print('enter array elements here with space')
list1 = [int(a) for a in input().split()]
x = int(input('please enter number you want to find.'))
sequential_search(list1,x)

# Ordered list:

def sequential_search(array, element):
    position = 0
    found = False
    stop = False
    while position < len(array) and not found and not stop:
        if array[position] == element:
            found = True
        else:
            if array[position] > element:
                stop = True
            else:
                position += 1
    print(found)
print('enter array elements here with space')
list1 = [int(a) for a in input().split()]
list1.sort()

temp = []
new_list = []
for i in list1:
    if i not in temp:
        temp.append(i)
        new_list.append(i)
temp = []

x = int(input('please enter number you want to find.'))
sequential_search(new_list, x)
