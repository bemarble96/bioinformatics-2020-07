import sys

cnt = 0
def count_PASS(file_name):
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            if line.startswith("#"):
                header - line.strip().split("\t")
                filt_idx
            splitted = line.strip().split("\t")
            if splitted[6] == "PASS":
                cnt +=1
print(cnt)            

