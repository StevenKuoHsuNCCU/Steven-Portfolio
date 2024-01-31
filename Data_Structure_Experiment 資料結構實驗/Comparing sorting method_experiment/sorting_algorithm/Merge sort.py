# MergeSort in Python
# https://www.programiz.com/dsa/merge-sort
# Average time complexity : O(nlogn)
# Space complexity : O(n)



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


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# 輸入 Dataframe
merge = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Merge sort.csv")
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")
hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")



# Experiment
'''
merge = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Merge sort.csv")    

timelist = list()


for i in range(0,10):
    print(i)
    data = list()
    for j in range(0,2**1):
        data.append(random.randint(1,1000))
    start = time.time()
    mergeSort(data)
    end = time.time()
    timelist.append(end-start)

merge["k = 1"]  = timelist

merge.to_csv("Merge sort.csv", index=False)
'''
# 平均資料

merge_avg = hw2_data[0:26]
x_merge = merge_avg["k"].values.reshape(-1,1)
y_merge = merge_avg["Merge sort"].values.reshape(-1,1)

## 訓練資料

merge_train = list()
k_train = list()

for i in range(0,26):
    for j in range(0,10):
        merge_train.append(merge.iloc[j,i])
        k_train.append(hw2_data["k"].iloc[i])

train_dict = {"train_k" : k_train,"train_counting" : merge_train}
train_data = pd.DataFrame(train_dict)


x_merge_train = train_data["train_k"].values.reshape(-1,1)
y_merge_train = train_data["train_counting"].values.reshape(-1,1)

## 預測資料
test_df = hw2_data[0:30]
test_data1 = test_df["k"].values.reshape(-1,1)


## 訓練不同次方多項式的迴歸模型

## 裝不同次方多項式的分數
scores = list()

## 設定欲實驗的次方項
polynomial_degree = list()
for i in range(1,20):
    polynomial_degree.append(i)

for index, num in enumerate(polynomial_degree):
  
  ## 訓練多項式迴歸模型
  regressor = make_pipeline(PolynomialFeatures(num), LinearRegression(fit_intercept=False))
  regressor.fit(x_merge_train,y_merge_train)
  ## 裝進精準度
  scores.append(regressor.score(x_merge,y_merge))
  


  ## 預測數據
  pred = regressor.predict(x_merge)
  
  ## 視覺化多項式迴歸模型線
  plt.plot(x_merge, regressor.predict(x_merge), label = 'Polynomial Degree ' + str(polynomial_degree[index]))
      
      
## 印出分數

max_index = scores.index(max(scores))  
print('Polynomial Degree ' + str(max_index+1) + ' Score: ' + str(scores[max_index]))
print(scores)

## 繪製數據集資料點
plt.scatter(x_merge,y_merge)
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
top_regression.fit(x_merge_train,y_merge_train)

## 預測數據
pred_data = regressor.predict(test_data1)

# 儲存預測數據
'''
for i in range(0,30):
    hw2_pred_data["Merge sort"].iloc[i] = pred_data[i][0]   
hw2_pred_data.to_csv("Assignment2_pred_data.csv", index=False)
'''
print(pred_data)


## 視覺化多項式迴歸模型線
plt.style.use("seaborn")
plt.plot(test_data1, regressor.predict(test_data1), color = "red", label = 'Regression Line (polynomial degree '+str(max_index+1)+")")
      
## 繪製數據集資料點
plt.scatter(x_merge,y_merge, color = "orange", label = "Testing average time")
plt.style.use("seaborn")
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.ticklabel_format(style="plain")
plt.title("The Best Regression Line")
plt.legend()
plt.show()

## Time complexity line
x = np.linspace(0, 30, 1000)
y = np.log(2**x)*(2**x)
plt.plot(x,y, color = "blue", label = "Time complexity O(nlogn)")
plt.style.use("seaborn")
plt.legend()
plt.title("The Time Complexity Line -- Merge Sort")
plt.ticklabel_format(style="plain")
plt.show()





