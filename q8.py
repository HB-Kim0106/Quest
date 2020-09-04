# !/usr/bin/python3

import sys

vcf =  sys.argv[1]

d_cnt = {}
l_length = []

def maxV(x):
    return d_cnt[x]

with open(vcf, "r") as handles:
    for line in handles:
        rowList = line.strip().split("\t")
        start = rowList[9].strip().split(",")
        end = rowList[10].strip().split(",")
        
        exon = 0 
        for i in range(len(start)-1):
            exon += int(end[i]) - int(start[i])

        l_length.append(exon)    
        d_cnt[rowList[1]] = exon
        
    key_max = max(d_cnt.keys(),key=maxV)
    print(key_max,d_cnt[key_max])




