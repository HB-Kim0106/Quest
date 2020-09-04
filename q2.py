# !/usr/bin/python3

import sys

gene = sys.argv[1]
data = sys.argv[2]

with open(data, "r") as handles1, open(gene, "r") as handles2:
    l_book = [] 
    for line1 in handles1:
        word = line1.strip().split("\t")
        for i in word:
            l_book.append(i)

    d_book = {}
    for j in range(0,len(l_book), 2):
        d_book[l_book[j]] = l_book[j+1]

    mylist  = handles2.read().splitlines()
    for line2 in mylist :
        if line2 in d_book:
            print(line2 + "\t" + d_book[line2])
        elif line2 not in d_book:
            print(line2 + "\t" +"NA")
