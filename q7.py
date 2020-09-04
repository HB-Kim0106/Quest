# !/usr/bin/python3
import sys

num = int(sys.argv[1])
    
my = [0, 1, 1]

for i in range(num+1):
    if i < 3:
        continue
    else:
        cat = my[i-1] + my[i-2] 
        my.append(cat)

print(my[num])
    
    
    
    

