def insertion_sort(list1):
    for i in range(1, len(list1)):
        current_val = list1[i]
        position = i
        while position > 0 and list1[position - 1] > current_val:
            list1[position] = list1[position - 1]
            position -= 1

        list1[position] = current_val
        print(list1)
print('please enter numbers with space as input')
x = [int(a) for a in input().split()]
insertion_sort(x)
