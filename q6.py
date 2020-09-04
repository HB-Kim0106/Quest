# !/usr/bin/python3

import sys

seq  = sys.argv[1]

with open(seq, "r") as handles:
    lines = handles.read().splitlines()
    l_seq = "" 
    for line in lines:
        if ">" in line:
            continue
        else:
            l_seq += line

    d_seq = {}
    for i in l_seq:
        if i not in d_seq:
            d_seq[i] = 0
            d_seq[i] += 1
        else:
            d_seq[i] += 1
    
    s_seq = sorted(d_seq.items(), key=lambda x: x[1], reverse=True)
    f_seq = s_seq[:5]

    for (j,k) in f_seq:
        print(j, ":", k, "\n")





