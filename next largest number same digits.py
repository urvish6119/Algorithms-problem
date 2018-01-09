import sys
x = int(input('enter number:'))
y = str(x)
z = len(y)
for i in range(z-1,0,-1):
    if y[i] > y[i-1]:
        break

if i == 1:
    print('not possible.')
    sys.exit()

greater = y[i-1]
smallest = i

for j in range(i+1,z):
    if y[j] > greater and y[j] < y[smallest]:
        smallest = j

list1 = list(y)
list1[smallest], list1[i-1] = list1[i-1], list1[smallest]
sorted1 = list1[0:i]
sorted2 = list1[i:len(list1)]
sorted2.sort()
ans1 = sorted1 + sorted2
ans = int(''.join(ans1))
print('Next greatest number with same digits is: {}'.format(ans))