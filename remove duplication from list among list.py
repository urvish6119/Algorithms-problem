list1 = [[1,2,1],[1,2,3,2,3],[0,2,-1],[1,1,0,1,3,3],[1,2,3,1,2],[0,1,0,-1,-1,0],[-1,0,-2,0,1,2,-2,2],[2,0,-1,3,-2,0,2,3],[1,2,3,1,2]]

temp = []
new_list = []
for j in list1:
    for k in j:
        if k not in temp:
            temp.append(k)

    new_list.append(temp)
    temp = []
print(new_list)