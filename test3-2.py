import sys
import json

def read_fasta(file_name):
    ret=""
    with open(file_name,'r') as handle:
         for line in handle:
             ret += line
    return ret

def to_json(l,file_name):
    with open(f"{file_name}.json", 'w') as handle:
        json.dump(l,handle,indent=4)

file_name = sys.argv[1]
ret = read_fasta(file_name)
ret1 = to_json(ret,file_name)

