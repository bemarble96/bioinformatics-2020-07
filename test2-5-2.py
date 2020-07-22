import sys

n = int(sys.argv[1])

base1 = ["A","C","G","T"]
base2 = ["A","C","G","T"]

list = []

def mer(base1,base2,n):
    if n ==1:
        return base2
    for i in base1:
        for p in base2:
            list.append(i+p)
    return mer(base1,list,n-1) 

print(mer(base1,base2,n))
#print(list) 
#print(ret)   
