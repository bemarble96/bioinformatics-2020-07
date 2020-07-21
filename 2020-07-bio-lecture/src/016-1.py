
import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python{sys.argv[0]} {fasta.gz}")
    sys.exit()

f = sys.argv[1]
d = {}
with gzip.open(f,'rb') as handle:
    for line in handle:
        line=line.decode("utf-8").strip()
        if line.startswith(">"):
            continue
        for s in line:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
with open("result.txt", 'w') as handle:
    handle.write(f"a: {d['A']

