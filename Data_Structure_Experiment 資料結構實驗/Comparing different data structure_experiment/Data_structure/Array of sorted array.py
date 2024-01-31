# Array of Sorted Array Implementation

# k = 25 (記憶體不足)


import random
import pandas as pd
import numpy as np
import time


"""************************************************************* Import dataframe ******************************************************************"""

add = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_add_data.csv")

search = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_search_data.csv")




"""************************************************************* Array of Sorted Array Inplementation ******************************************************************"""


Array_of_sorted_Array = dict()

    
def BinarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

    
def ASA_Insert(n):
    
    p_empty = 1
    
    temp = [n]
    while True:           #建造一個 while loop 從第一層往下看，只要是滿的就跟input merge ，遇到空的就放進去並跳出迴圈。
        
        
        try:
            temp = Array_of_sorted_Array[p_empty] + temp
        
        except:
            Array_of_sorted_Array[p_empty] = temp
            p_empty = 1
            break
        
        temp = sorted(temp)
        del Array_of_sorted_Array[p_empty]
        p_empty += 1


def ASA_Search(n):
    for i in sorted(list(Array_of_sorted_Array)):
        search_result = BinarySearch(Array_of_sorted_Array[i], n, 0, len(Array_of_sorted_Array[i])-1)
        if search_result >= 0:
            return 1
        else:
            pass
    return 0
    


"""************************************************************* Experiment add ******************************************************************"""


#test variable
x = 24




start_add = time.time()

for i in range(0,2**x-1):
  ASA_Insert(random.randint(1,2**30))
    
end_add = time.time()

add_time =  end_add - start_add
add["Array of sorted array"].iloc[x-15] = add_time






"""************************************************************* Experiment (search) ******************************************************************"""

start_search = time.time()

for i in range(0,100000):
  temp = ASA_Search(random.randint(1,2**30+1))
    
end_search = time.time()
    
search_time = (end_search - start_search)
search["Array of sorted array"].iloc[x-15] = search_time

print(Array_of_sorted_Array)
print("add time:",add_time)
print("search time:",search_time)


"""************************************************************* Save data ******************************************************************"""

#add.to_csv("HW3_add_data.csv", index=False)
#search.to_csv("HW3_search_data.csv", index=False)




















    
    
           
                
        





