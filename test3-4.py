import sys

def count_base(file_name):
    d = {}
    l = []
    with open(file_name,'r') as handle:
        for line in handle:
            ret = line.strip().split(">")
            for i in range(0,len(ret)):
                if i % 2 == 1:
                    continue
                l.append(ret[i])
                for p in l:
                    d[p] = len(p)


    return d

file_name = sys.argv[1]
d = count_base(file_name)
print(d)
