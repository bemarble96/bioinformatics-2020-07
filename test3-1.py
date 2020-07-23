import sys

file_name = sys.argv[1]
def count_base(file_name):
    seq = ""
    d = {}
    A_cnt = 0
    C_cnt = 0
    G_cnt = 0
    T_cnt = 0
    with open(file_name ,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            seq +=line.strip()
            for i in seq:
                if i == "A":
                    A_cnt += 1
                    d[i]= A_cnt
                elif i == "T":
                    T_cnt += 1
                    d[i]= T_cnt
                elif i == "G":
                    G_cnt += 1
                    d[i]= G_cnt
                elif i == "C":
                    C_cnt += 1
                    d[i]= C_cnt
    return d
d = count_base(file_name)
print(d)

