import sys

num = sys.argv[1]
num0 = 1

for i in range(1,int(num)+1):
    num0 *= i

print(num0)

