import sys

file_name = sys.argv[1]                      
d ={}
with open(file_name,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line:
            if s in d:
                d[s] += 1
            else:
               d[s] = 1
with open ("059.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"C: {d['C']}\n")

