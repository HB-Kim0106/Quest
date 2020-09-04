#!/usr/bin/python3

import sys

data = sys.argv[1]

with open(data, "r") as handles:
    lines = handles.readlines()
    l_genome = []
    for num in range(len(lines)):
        if ">" in lines[num]:
            l_genome.append(lines[num])
        
        else:
            if ">" in lines[num-1]:
                l_genome.append(lines[num])
            
            else:
                l_genome[-1] += lines[num]



    for line2 in l_genome:
        if ">" in line2:
            continue
        else:
            G = line2.count("G")
            C = line2.count("C")
            GC = round((G+C)/len(line2) * 100, 1) 
        print(GC)

