# !/usr/bin/python3

import sys

vcf = sys.argv[1]

with open(vcf,"r") as handles:
    cnt = 0
    for line in handles: 
        if line.startswith("#"):
            continue
        else:
            l_list = line.strip().split("\t")
            if l_list[6] == "PASS":
                cnt += 1

    print(cnt)

