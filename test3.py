import sys

d = {"A":"Adenine","C":"Cytosine", "G":"Guanine","T":"Thymine","U":"Uracil"}

sequence = sys.argv[1]

for i in sequence:
    d[i]

print(d[i])
    
