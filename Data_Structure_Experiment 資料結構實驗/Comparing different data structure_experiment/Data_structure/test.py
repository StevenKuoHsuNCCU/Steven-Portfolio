# Python3 code for searching and deleting element in skip list
import treap
import random
import pandas as pd
import numpy as np
import time



add = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_add_data.csv")

search = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_search_data.csv")





for i in range(0,16):
    add["k (2**k)"].iloc[i] = 2**(add["k (2**k)"].iloc[i])
    search["k (2**k)"].iloc[i] = 2**(search["k (2**k)"].iloc[i])


print(add)



#add.to_csv("HW3_add_data.csv", index=False)
#search.to_csv("HW3_search_data.csv", index=False)
