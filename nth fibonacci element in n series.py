def fib(number,answer):
    list2 = []
    for i in range(number,answer):
        if i == number:
            if i == 0:
                list2.append(i)
                list2.append(1)
            else:
                list2.append(i)
                list2.append(i)
        else:
            # I have use answer which gives element counting from 1 as beginning not 0,
            # if you want to count from 0 as beginning then enter answer-1 and change answer-2 in output line.
            for j in range(2,answer):
                j = list2[j-1]+list2[j-2]
                list2.append(j)
            print(list2)
            print(list2[answer-1])
            break

x = int(input('please enter number to generate fibonacci series:'))
y = int(input('Please enter which element from fibonacci series you want to see:'))
fib(x,y)