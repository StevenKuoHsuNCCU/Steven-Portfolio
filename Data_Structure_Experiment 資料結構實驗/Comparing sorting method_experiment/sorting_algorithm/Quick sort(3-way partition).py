# python3 program for 3-way quick sort
# https://gist.github.com/adonese/4bf34d5b57ee0358626c

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

def partition3(A, l, r):

    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt



def quick_sort(A, l, r):
    """
    quick_sort: One of the most used sorting algorithm. 
    It makes to recursive calls. One to sort the left part separately, other for sorting the right part.
    The partition key is chosen randomly via ``random.randint(l, r)`` and it's between the ``l,  r``.
    
    PARAMETERS:
    -----------
    A: Array or the sequence that we want to sort.
    l: The lower bound of the array that we want to sort. It's not very important we might replace it by a wrapper function
    that only takes in an array as input. In this case it's the first element in the left part of the array.
    r: It's the same as l, only differs as it's the first element from the end.
    
    RETURNS:
    -------
    Sorted list A.
    """
    if l >= r: 
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    
    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)  
    
# 輸入 Dataframe
three_way = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_3 way partition.csv")
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")
hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")


    
# Experiment
'''
Three_way = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_3 way partition.csv")    

timelist = list()


for i in range(0,10):
    print(i)
    data = list()
    for j in range(0,2**14):
        data.append(random.randint(1,1000))
    n = len(data)
    start = time.time()
    quick_sort(data,0,n-1)
    end = time.time()
    timelist.append(end-start)


Three_way["k = 14"]  = timelist

Three_way.to_csv("Quick sort_3 way partition.csv", index=False)
'''


# 平均資料

three_way_avg = hw2_data[0:27]
x_three_way = three_way_avg["k"].values.reshape(-1,1)
y_three_way = three_way_avg["Quick sort (3 way partition)"].values.reshape(-1,1)

## 訓練資料

three_way_train = list()
k_train = list()

for i in range(0,27):
    for j in range(0,10):
        three_way_train.append(three_way.iloc[j,i])
        k_train.append(hw2_data["k"].iloc[i])

train_dict = {"train_k" : k_train,"train_three_way" : three_way_train}
train_data = pd.DataFrame(train_dict)


x_three_way_train = train_data["train_k"].values.reshape(-1,1)
y_three_way_train = train_data["train_three_way"].values.reshape(-1,1)

## 預測資料
test_df = hw2_data[0:30]
test_data1 = test_df["k"].values.reshape(-1,1)



## 訓練不同次方多項式的迴歸模型

## 裝不同次方多項式的分數
scores = list()

## 設定欲實驗的次方項
polynomial_degree = list()
for i in range(1,10):
    polynomial_degree.append(i)

for index, num in enumerate(polynomial_degree):
  
  ## 訓練多項式迴歸模型
  regressor = make_pipeline(PolynomialFeatures(num), LinearRegression(fit_intercept=False))
  regressor.fit(x_three_way_train,y_three_way_train)
  ## 裝進精準度
  scores.append(regressor.score(x_three_way,y_three_way))
  


  ## 預測數據
  pred = regressor.predict(x_three_way)
  
  ## 視覺化多項式迴歸模型線
  plt.plot(x_three_way, regressor.predict(x_three_way), label = 'Polynomial Degree ' + str(polynomial_degree[index]))
      
      
## 印出分數
max_index = scores.index(max(scores))  
print('Polynomial Degree ' + str(max_index+1) + ' Score: ' + str(scores[max_index]))

## 繪製數據集資料點
plt.scatter(x_three_way,y_three_way)
plt.style.use("seaborn")
plt.ticklabel_format(style="plain")
plt.legend()
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.title("Training the Regression Line")
plt.show()


## 最佳預測迴歸
top_regression = make_pipeline(PolynomialFeatures(max_index+1), LinearRegression(fit_intercept=False))
## 訓練最佳預測迴歸模型
top_regression.fit(x_three_way_train,y_three_way_train)

## 預測數據
pred_data = regressor.predict(test_data1)

# 儲存預測數據
'''
for i in range(0,30):
    hw2_pred_data["Quick sort (3 way partition)"].iloc[i] = pred_data[i][0]   
hw2_pred_data.to_csv("Assignment2_pred_data.csv", index=False)
'''
print(pred_data)


## 視覺化多項式迴歸模型線
plt.style.use("seaborn")
plt.plot(test_data1, regressor.predict(test_data1), color = "red", label = 'Regression Line (polynomial degree '+str(max_index+1)+")")
      
## 繪製數據集資料點
plt.scatter(x_three_way,y_three_way, color = "orange", label = "Testing average time")
plt.style.use("seaborn")
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.ticklabel_format(style="plain")
plt.title("The Best Regression Line")
plt.legend()
plt.show()




    