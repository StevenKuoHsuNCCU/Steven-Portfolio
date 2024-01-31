# Insertion sort 
# https://www.programiz.com/dsa/insertion-sort
# Average time complexity : O(n^2)
# Space complexity : O(1)

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

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].    
            
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


# 輸入 Dataframe
insertion = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Insertion sort.csv")    
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")
hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")



# Experiment
'''
timelist = list()


for i in range(0,10):
    print(i)
    data = list()
    for j in range(0,2**1):
        data.append(random.randint(1,1000))
    start = time.time()
    insertionSort(data)
    end = time.time()
    timelist.append(end-start)


insertion["k = 1"]  = timelist
insertion.to_csv("Insertion sort.csv", index=False)
'''


# 平均資料

insertion_avg = hw2_data[0:18]
x_insertion = insertion_avg["k"].values.reshape(-1,1)
y_insertion = insertion_avg["Insertion sort"].values.reshape(-1,1)



## 訓練資料

insertion_train = list()
k_train = list()

for i in range(0,18):
    for j in range(0,10):
        insertion_train.append(insertion.iloc[j,i])
        k_train.append(hw2_data["k"].iloc[i])

train_dict = {"train_k" : k_train,"train_insertion" : insertion_train}
train_data = pd.DataFrame(train_dict)


x_insertion_train = train_data["train_k"].values.reshape(-1,1)
y_insertion_train = train_data["train_insertion"].values.reshape(-1,1)

## 預測資料
test_df = hw2_data[0:30]
test_data1 = test_df["k"].values.reshape(-1,1)

test_list = list()
for i in range(0,2**18,100):
    test_list.append(i)
test_dict = {"testing":test_list}
test_data2 = pd.DataFrame(test_dict)



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
  regressor.fit(x_insertion_train,y_insertion_train)
  ## 裝進精準度
  scores.append(regressor.score(x_insertion,y_insertion))
  


  ## 預測數據
  pred = regressor.predict(x_insertion)
  
  ## 視覺化多項式迴歸模型線
  plt.style.use("seaborn")
  plt.plot(x_insertion, regressor.predict(x_insertion), label = 'Polynomial Degree ' + str(polynomial_degree[index]))
      
      
## 印出分數
max_index = scores.index(max(scores))  
print('Polynomial Degree ' + str(max_index+1) + ' Score: ' + str(scores[max_index]))

## 繪製數據集資料點
plt.scatter(x_insertion,y_insertion)
plt.ticklabel_format(style="plain")
plt.style.use("seaborn")
plt.legend()
plt.xlabel("2^k data in a unsorted array")
plt.title("Training the Regression Line")
plt.ylabel("time(s)")
plt.show()


## 最佳預測迴歸
top_regression = make_pipeline(PolynomialFeatures(max_index+1), LinearRegression(fit_intercept=False))
## 訓練最佳預測迴歸模型
top_regression.fit(x_insertion_train,y_insertion_train)

## 預測數據
pred_data = regressor.predict(test_data1)

# 儲存預測數據
'''
for i in range(0,30):
    hw2_pred_data["Insertion sort"].iloc[i] = pred_data[i][0]   
hw2_pred_data.to_csv("Assignment2_pred_data.csv", index=False)
'''
print(pred_data)


## 視覺化多項式迴歸模型線
plt.plot(test_data1, regressor.predict(test_data1), color = "red", label = 'Regression Line (polynomial degree '+str(max_index+1)+")")
      
## 繪製數據集資料點
plt.scatter(x_insertion,y_insertion, color = "orange", label = "Testing average time")
plt.style.use("seaborn")
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.ticklabel_format(style="plain")
plt.legend()
plt.title("The Best Regression Line")
plt.show()


## Time complexity line
x = np.linspace(0, 30, 1000)
y = (2**x)**2
plt.plot(x,y, color = "blue", label = "Time complexity O(n-square)")
plt.style.use("seaborn")
plt.title("The Time Complexity Line -- Insertion Sort")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()










