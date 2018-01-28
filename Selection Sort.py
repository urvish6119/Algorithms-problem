def selection_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_pos = 0
        for j in range(1, i + 1):
            if arr[j] > arr[max_pos]:
                max_pos = j
        arr[i], arr[max_pos] = arr[max_pos], arr[i]
        print(arr)
print('please enter numbers with space as input')
x = [int(a) for a in input().split()]
selection_sort(x)
