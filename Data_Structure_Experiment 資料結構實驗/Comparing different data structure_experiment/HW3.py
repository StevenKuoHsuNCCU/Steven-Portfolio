import random
import pandas as pd
import numpy as np
import time
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split


"""************************************************************* Import dataframe ******************************************************************"""

add = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_add_data.csv")

search = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_search_data.csv")








"""************************************************************* Time Complexity Line  ******************************************************************"""

plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
"""

#
## Time complexity line
x = np.linspace(15, 24, 1000)
y = x*(2**x)/10066329
plt.plot(x,y, color = "red", label = "Time complexity O(logn)")

plt.show()

"""

"""************************************************************* Search Regression Line ( BTree ) ******************************************************************"""

# 畫圖資料


x_btree_search = search["k (2**k)"].iloc[0:10]
y_btree_search = search["BTree"].iloc[0:10]

  
plt.plot(x_btree_search, y_btree_search,color = "blue", label =  'BTree Regression Line --Search')
      
      

## 繪製數據集資料點
plt.scatter(x_btree_search,y_btree_search)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("BTree Search Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 24, 1000)
y = x*(2**x)/(1788550838*1.1)+0.078
plt.plot(x,y, color = "red", label = "Time complexity O(logn)--(y = x*(2**x)/(1788550838*1.1)+0.078)")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Insertion Regression Line ( BTree ) ******************************************************************"""

# 畫圖資料


x_btree_add = add["k (2**k)"].iloc[0:10]
y_btree_add = add["BTree"].iloc[0:10]

  
plt.plot(x_btree_add, y_btree_add, color = "blue", label =  'BTree Regression Line --Insertion')
      
      

## 繪製數據集資料點
plt.scatter(x_btree_add,y_btree_add)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("BTree Insertion Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 24, 1000)
y = x*(2**x)/10066329
plt.plot(x,y, color = "red", label = "Time complexity O(logn)--(y = x*(2**x)/10066329)")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()




"""************************************************************* Search Regression Line ( Skip List ) ******************************************************************"""

# 畫圖資料


x_skiplist_search = search["k (2**k)"].iloc[0:9]
y_skiplist_search = search["Skip List"].iloc[0:9]

  
plt.plot(x_skiplist_search, y_skiplist_search,color = "blue", label =  'Skip List Regression Line --Search')
      
      

## 繪製數據集資料點
plt.scatter(x_skiplist_search,y_skiplist_search)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Skip List Search Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 23, 1000)
y = x*(2**x)/(1788550838/22)+0.31
plt.plot(x,y, color = "red", label = "Time complexity O(logn)--(y = x*(2**x)/(1788550838/22)+0.31)")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Insertion Regression Line ( Skip List ) ******************************************************************"""

# 畫圖資料


x_skiplist_add = add["k (2**k)"].iloc[0:9]
y_skiplist_add = add["Skip List"].iloc[0:9]

  
plt.plot(x_skiplist_add, y_skiplist_add, color = "blue", label =  'Skip List Regression Line --Insertion')
      
      

## 繪製數據集資料點
plt.scatter(x_skiplist_add,y_skiplist_add)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Skip List Insertion Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 23, 1000)
y = x*(2**x)/(10066329/8)
plt.plot(x,y, color = "red", label = "Time complexity O(logn)--(y = x*(2**x)/(10066329/8))")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()






"""************************************************************* Search Regression Line ( Treap ) ******************************************************************"""

# 畫圖資料


x_treap_search = search["k (2**k)"].iloc[0:9]
y_treap_search = search["Treap"].iloc[0:9]

  
plt.plot(x_treap_search, y_treap_search,color = "blue", label =  'Treap Regression Line --Search')
      
      

## 繪製數據集資料點
plt.scatter(x_treap_search,y_treap_search)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Treap Search Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 23, 1000)
y = x*(2**x)/(1788550838/4)+0.175
plt.plot(x,y, color = "red", label = "Time complexity O(logn)--(y = x*(2**x)/(1788550838/4)+0.175)")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Insertion Regression Line ( Treap ) ******************************************************************"""

# 畫圖資料


x_treap_add = add["k (2**k)"].iloc[0:9]
y_treap_add = add["Treap"].iloc[0:9]

  
plt.plot(x_treap_add, y_treap_add, color = "blue", label =  'Treap Regression Line --Insertion')
      
      

## 繪製數據集資料點
plt.scatter(x_treap_add,y_treap_add)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Treap Insertion Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 23, 1000)
y = x*(2**x)/(10066329/5)
plt.plot(x,y, color = "red", label = "Time complexity O(logn)--(y = x*(2**x)/(10066329/5))")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Search Regression Line ( Hash Table ) ******************************************************************"""

# 畫圖資料


x_hashtable_search = search["k (2**k)"].iloc[0:11]
y_hashtable_search = search["Hash Table"].iloc[0:11]

  
plt.plot(x_hashtable_search, y_hashtable_search,color = "blue", label =  'Hash Table Regression Line --Search')
      
      

## 繪製數據集資料點
plt.scatter(x_hashtable_search,y_hashtable_search)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Hash Table Search Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 25, 1000)
y = (2**x)/(1788550838/3.5)+0.058
plt.plot(x,y, color = "red", label = "Time complexity O(1)--(y = (2**x)/(1788550838/3.5)+0.058)")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Insertion Regression Line ( Hash Table ) ******************************************************************"""

# 畫圖資料


x_hashtable_add = add["k (2**k)"].iloc[0:11]
y_hashtable_add = add["Hash Table"].iloc[0:11]

  
plt.plot(x_hashtable_add, y_hashtable_add, color = "blue", label =  'Hash Table Regression Line --Insertion')
      
      

## 繪製數據集資料點
plt.scatter(x_hashtable_add,y_hashtable_add)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Hash Table Insertion Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 25, 1000)
y = (2**x)/(10066329/8)
plt.plot(x,y, color = "red", label = "Time complexity O(1)--(y = (2**x)/(10066329/8))")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Search Regression Line ( Array of Sorted Array ) ******************************************************************"""

# 畫圖資料


x_asa_search = search["k (2**k)"].iloc[0:11]
y_asa_search = search["Array of sorted array"].iloc[0:11]

  
plt.plot(x_asa_search, y_asa_search,color = "blue", label =  'Array of Sorted Array Regression Line --Search')
      
      

## 繪製數據集資料點
plt.scatter(x_asa_search,y_asa_search)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Array of Sorted Array Search Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 25, 1000)
y = x*x/(1000)
plt.plot(x,y, color = "red", label = "Time complexity O(logn*logn)--(y = x*x/(1000))")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Insertion Regression Line ( Skip List ) ******************************************************************"""

# 畫圖資料


x_asa_add = add["k (2**k)"].iloc[0:11]
y_asa_add = add["Array of sorted array"].iloc[0:11]

  
plt.plot(x_asa_add, y_asa_add, color = "blue", label =  'Array of Sorted Array Regression Line --Insertion')
      
      

## 繪製數據集資料點
plt.scatter(x_asa_add,y_asa_add)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data")
plt.title("Array of Sorted Array Insertion Experiment")
plt.ylabel("time(s)")


#
## Time complexity line
x = np.linspace(15, 25, 1000)
y = x*(2**x)/(10066329*2)
plt.plot(x,y, color = "red", label = "Time complexity O(logn)---(y = x*(2**x)/(10066329*2))")
plt.style.use("seaborn")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


"""************************************************************* Search Graph ******************************************************************"""

# 畫圖資料


plt.ticklabel_format(style="plain")
plt.style.use("seaborn")


  
plt.plot(x_asa_search, y_asa_search, label =  'Array of Sorted Array')
plt.plot(x_btree_search, y_btree_search, label =  'BTree')
plt.plot(x_hashtable_search, y_hashtable_search, label =  'Hash Table ')
plt.plot(x_treap_search, y_treap_search, label =  'Treap')
plt.plot(x_skiplist_search, y_skiplist_search, label =  'Skip List')

      

## 繪製數據集資料點

plt.xlabel("2^k data")
plt.title("Search Experiment")
plt.ylabel("time(s)")
plt.ylim(0,0.75)
plt.legend()
plt.show()


"""************************************************************* Insertion Graph ******************************************************************"""

# 畫圖資料

plt.ticklabel_format(style="plain")
plt.style.use("seaborn")


  
plt.plot(x_asa_add, y_asa_add,  label =  'Array of Sorted Array ')
plt.plot(x_btree_add, y_btree_add,  label =  'BTree')
plt.plot(x_skiplist_add, y_skiplist_add,  label =  'Skip List ')
plt.plot(x_treap_add, y_treap_add, label =  'Treap ')
plt.plot(x_hashtable_add, y_hashtable_add,  label =  'Hash Table')

      

## 繪製數據集資料點


plt.xlabel("2^k data")
plt.title("Insertion Experiment")
plt.ylabel("time(s)")
plt.ylim(0,50)
plt.legend()



plt.show()















