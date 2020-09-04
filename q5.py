# !/usr/bin/python3

import sys

vcf = sys.argv[1]

with open(vcf,"r") as handles:
    for line in handles: 
        if line.startswith("#"):
            continue
        else:
            l_list = line.strip().split("\t")
            chrom = l_list[0]
            pos = l_list[1]
            GT= l_list[9].strip().split(":")
            ref = l_list[3]
            alt = l_list[4].strip().split(",")
            book = []
            book += ref 
            book += alt
            alpha = ""
            if "/" in GT[0]:
                unpase = GT[0].strip().split("/") #0/1 => unpase = [0, 1]
                M1 = book[int(unpase[0])]
                P1 = book[int(unpase[1])] 
                alpha += (M1 + "/" + P1)

            elif "|" in GT[0]:
                pase = GT[0].strip().split("|")
                M2 = book[int(pase[0])]
                P2 = book[int(pase[1])] 
                alpha  += (M2 + "|" + P2) 

            print(chrom,pos,GT[0],alpha,sep = "\t")


