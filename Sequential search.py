# Unordered list:
def sequential_search(list1, element):
    position = 0
    found = False
    while position < len(list1) and not found:
        if list1[position] == element:
            found = True
        else:
            position += 1
    print(found)
print('enter array elements here with space')
list_i = [int(a) for a in input().split()]
x = int(input('please enter number you want to find.'))
sequential_search(list_i,x)

# Ordered list:

def sequential_search(list1, element):
    position = 0
    found = False
    stop = False
    while position < len(list1) and not found and not stop:
        if list1[position] == element:
            found = True
        else:
            if list1[position] > element:
                stop = True
            else:
                position += 1
    print(found)
print('enter array elements here with space')
list_i = [int(a) for a in input().split()]
list_i.sort()

temp = []
new_list = []
for i in list_i:
    if i not in temp:
        temp.append(i)
        new_list.append(i)
temp = []

x = int(input('please enter number you want to find.'))
sequential_search(new_list, x)
