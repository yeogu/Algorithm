N = int(input())

mok = int(N / 4)
namegi = int(N % 4)
str = ""
for i in range(mok):
    str += "long "
if namegi != 0:
    str += "long "
str += "int"
print(str)