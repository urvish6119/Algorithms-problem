# this is just half implemented as it uses only multiplications not addition.

x = int(input('Enter the amount:'))

print('Enter numbers you to make different ways to make amount with space')
y = [int(a) for a in input().split()]

factors = []

for i in range(1, x+1):
    if x % i == 0:
        factors.append(i)
print(factors)

new_factor = []

for j in y[0:]:
    for k in factors[0:]:
        if j == k:
            new_factor.append(j)
print(new_factor)

for l in new_factor:
    nums = x/l
    print(str(l) * int(nums))
