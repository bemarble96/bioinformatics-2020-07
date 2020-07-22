import sys

f = "059.fasta"

A,C,G,T = 0,0,0,0

with open(file_name,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            header = line.strip()
        else:
            seq = line.strip()
            A += seq.count("A")
            T += seq.count("T")
            C += seq.count("C")
            G += seq.count("G")
print(f"A: {A}")
print(f"T: {T}")
print(f"C: {C}")
print(f"G: {G}")
