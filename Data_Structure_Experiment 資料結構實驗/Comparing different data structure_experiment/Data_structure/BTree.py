# BTree Implementattion

# k = 24 (記憶體不足)



import treap
import random
import pandas as pd
import numpy as np
import time
from BTrees._OOBTree import OOBTree


"""************************************************************* Import dataframe ******************************************************************"""

add = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_add_data.csv")

search = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_search_data.csv")



"""************************************************************* Experiment add ******************************************************************"""


#test variable
x = 25


B = OOBTree()


start_add = time.time()

for i in range(0,2**x):
  B.update({random.randint(1,2**30+1) : i})
    
end_add = time.time()

add_time =  end_add - start_add
add["BTree"].iloc[x-15] = add_time






"""************************************************************* Experiment (search) ******************************************************************"""

start_search = time.time()

for i in range(0,100000):
  temp = B.has_key(random.randint(1,2**30+1))
    
end_search = time.time()
    
search_time = (end_search - start_search)
search["BTree"].iloc[x-15] = search_time



print("add time:",add_time)
print("search time:",search_time)


"""************************************************************* Save data ******************************************************************"""

add.to_csv("HW3_add_data.csv", index=False)
search.to_csv("HW3_search_data.csv", index=False)





