from ast import Index
import ctypes as c
from operator import index
import random as rd
import time
import sys
from turtle import color
import matplotlib.pyplot as plt
import math 
import pandas as pd
from matplotlib import ticker
pd.set_option('float_format', lambda x: '%.6f' % x)
import seaborn as sns



n = pd.read_csv("25store.csv")

'''


# plot the modify graph
log = list()
for i in range(0,2**25):
    log.append(math.log2(i+1))
n["log"] = log

k = n[["Dynamic array store","Linked list store"]]
k.index = n["log"]
k.plot(xlabel="N",ylabel="t(s)")
plt.show()
'''

r0_10 = 0
r10_100 = 0
r100_1000 = 0
r1000_10000 = 0
r10000_100000 = 0


for i in range(0,2**25):
    y = n["dd"][i]*1000000
    if 0 <= y  and y< 10: 
        r0_10 = r0_10+1
        continue
    if 10 <= y  and y < 100:
        r10_100 = r10_100 +1
        continue
    if 100 <= y  and y < 1000:
        r100_1000 = r100_1000 +1
        continue
    if 1000 <= y and y < 10000:
        r1000_10000  = r1000_10000 +1
        continue
    if 10000 <= y:
        r10000_100000 = r10000_100000 +1
        continue
    
print(r0_10)
print(r10_100)
print(r100_1000)
print(r1000_10000)
print(r10000_100000)

aa = list[r0_10,r10_100,r100_1000,r1000_10000,r10000_100000]
aaa = list["r0_10","r10_100","r100_1000","r1000_10000","r10000_100000"]
bb = pd.DataFrame()
bb["x"] = aa

bb.plot(kind="hist")









'''

a = pd.read_csv("Dyarr LL logk time.csv")
b = a[["Dt1","Lt1"]]
b.plot()
plt.show()

'''








