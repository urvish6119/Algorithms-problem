def selection_sort(list1):
    for i in range(len(list1) - 1, 0, -1):
        max_pos = 0
        for j in range(1, i + 1):
            if list1[j] > list1[max_pos]:
                max_pos = j
        list1[i], list1[max_pos] = list1[max_pos], list1[i]
        print(list1)
print('please enter numbers with space as input')
x = [int(a) for a in input().split()]
selection_sort(x)
