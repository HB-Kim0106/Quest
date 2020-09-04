#!/usr/bin/python3

import sys
import pandas as pd

tsv = sys.argv[1]

with open(tsv, "r") as handle:
    data = pd.read_csv(handle, sep = "\t")
    df = pd.DataFrame(data)
    del df['sample1']
    df.sort_values(by=['sample2'], axis=0, ascending=False,inplace=True)    
    df2 = df.head(5)
    df3 = df2.to_string(index=False)
    print(df3)
    
