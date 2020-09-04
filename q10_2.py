# !/usr/bin/python3

import sys

gene = sys.argv[1]

undupl = []
with open(gene, "r") as handle:
    lines1 = handle.readlines()
    for line in lines1:
        if lines1.count(line) == 1:
            undupl.append(line)
        
        elif lines1.count(line) >= 2:
            continue

    print(len(undupl))
    
