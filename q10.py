# !/usr/bin/python3

import sys

gene = sys.argv[1]

with open(gene, "r") as handle:
    lines1 = handle.readlines()
    line2 = set(lines1)
    print(len(line2))
