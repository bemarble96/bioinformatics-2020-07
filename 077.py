total = 0

with open ("077.bed", 'r') as handle:
    for line in handle:
        chrom_start_end = line.strip().split("\t")
        start = int(chrom_start_end[1])
        end = int(chrom_start_end[2])
        total += end - start

print(total)
