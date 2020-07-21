import sys

file_name = sys.argv[1]
l = ""

with open(file_name,'r') as handle:
    for line in handle:
        for s in line:
            l += s
            list = l.split("+")
print(len(list))

                        

