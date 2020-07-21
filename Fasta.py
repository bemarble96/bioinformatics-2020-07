class FASTA:
    def __init__(self, file_name) :
        self.file_name = file_name
        self.count = {}
    def count_base(self):
        with open(self.file_name, 'r') as handle:
           for line in handle:
               if line.startswith(">"):
                   continue
               line = line.strip()
               for s in line.strip()
                   if s in self.count:
                       self.count[s] += 1
                   else:
                       self.count[s] = 1 
    def__len__(self):
        for k,v in self.count.items():
            self.length += v
        return self.length
if __name__ =="__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} {fasta})
        sys.exit()
    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    print(t,count)
    print(len(t))
