import sys
import json

def read_csv(file_name:str) ->list:
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("s"):
                samples = line.strip().split(",")
                continue
            value =line.strip().split(",") # map() int()
            d = dict(zip(samples, value))
            ret= d
    return ret

def to_json(l:list,file_name:str) -> None:
    with open("test2-4.json",'w') as handle: # 저장할 이름을 지정
        json.dump(l,handle)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("#usage: python{sys.argv[0])[txt]")
        sys.exit()
file_name = sys.argv[1]
ret = read_csv(file_name)
ret = to_json(ret,file_name)
