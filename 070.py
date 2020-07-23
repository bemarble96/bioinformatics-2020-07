import sys


def count_read(file_name):
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            ret.append(line.strip())
    return ret
file_name = sys.argv[1]
vcf = count_read(file_name)

print(len(vcf))
