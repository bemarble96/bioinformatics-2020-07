import sys

file_name = sys.argv[1]
def comp_base(file_name):
    seq = ""
    comp = ""
    d = {"A":"T","T":"A","C":"G","G":"C"}
    with open(file_name ,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            seq +=line.strip()
            for i in seq:
                comp += d[i] 
    return comp


comp = comp_base(file_name)
print(comp)


