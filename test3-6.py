cnt =0
 
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            id_idx = header.index("ID")
            continue
        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alts = splitted[4]
        for alt in alts:
            cnt += 1
print(cnt)
