import pandas as pd
import re

# fg= open("getci.txt",'r',encoding='utf8',errors='ignore')
#
# for sentence in fg.readlines():
#     sentence=sentence.replace("\n","")
#     print(sentence)

getci=pd.read_csv('getci.csv',error_bad_lines=False)
getcisorted=getci.sort(["词频"],ascending=False)
getcisorted=getcisorted.fillna('NULL')
print(getcisorted)
getcisorted.to_csv('getcisorted.csv',header=None,index=None)
