x = int(input('please enter number:'))
binary = bin(x)
temp_len = binary[2:]
length = len(temp_len)
print(length)
# or you can also type like this:
x = int(input('please enter number:'))
binary = bin(x)[2:]
length = len(binary)
print(length)