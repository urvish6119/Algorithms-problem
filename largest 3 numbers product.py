print('please enter 3 or more number of integers you want, with space')
list1 = [int(a) for a in input().split()]

def product_of_3(list_items):

    if len(list_items) < 3:
        raise Exception('not 3 numbers.')

    highest_2 = max(list_items[0],list_items[1])
    lowest_2 = min (list_items[0], list_items[1])

    highest_product_2 = list_items[0] * list_items[1]
    lowest_product_2 = list_items[0] * list_items[1]

    highest_product_3 = list_items[0] * list_items[1] * list_items[2]

    for current in list_items[2:]:
        highest_product_3 = max(highest_product_3, current * highest_product_2, current * lowest_product_2)

        highest_product_2 = max(highest_product_2, current * highest_2, current * lowest_2)

        lowest_product_2 = min(lowest_product_2, current * highest_2, current * lowest_2)

        highest_2 = max(highest_2, current)
        lowest_2 = min(lowest_2, current)

    return highest_product_3

print(product_of_3(list1))