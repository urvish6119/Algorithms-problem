def bubble_sort(list1):
    for i in range(len(list1)-1, 0, -1):
        for k in range(i):
            if list1[k] > list1[k+1]:
                list1[k], list1[k+1] = list1[k+1], list1[k]
    print(list1)
print('please enter numbers with space as input')
x = [int(a) for a in input().split()]
bubble_sort(x)
