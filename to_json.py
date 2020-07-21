import sys
import json

def to_json(l):
    with open("read_sample.json,'w') as handle:
        json.dump(l,handle,ident=4)

 
