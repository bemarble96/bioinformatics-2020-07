#! /usr/bin/env python

with open("read_samples.py", 'r') as handle:
    for line  in handle:
        if line.startswith(">") :
            continue
        print(line.strip())
