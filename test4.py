import sys

n = sys.argv[1]
try:    
    if n.isdigit():
        result = 10/int(n)
    else:
        print(f"{n} is not number..please check.")   
except ZeroDivisionError:
    print(f"{n} is Zero..please check.")
    
print(result)

