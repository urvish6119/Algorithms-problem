print('please enter integers with space')
x = [int(a) for a in input().split()]
mul = 1
ans = []
for y in x[0:]:
    for z in x[0:]:
        if y != z:
            mul *= z
    ans.append(mul)
    mul = 1
print(ans)