# Counting sort in Python programming
# https://www.programiz.com/dsa/counting-sort
# Average time complexity : O(n+k)
# Space complexity : O(max)

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

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 1001

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 1001):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


# 輸入 Dataframe
counting = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Counting sort.csv")    
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")
hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")



# Experiment
'''

timelist = list()


for i in range(0,10):
    print(i)
    data = list()
    for j in range(0,2**14):
        data.append(random.randint(1,1000))
    start = time.time()
    countingSort(data)
    end = time.time()
    timelist.append(end-start)


counting["k = 14"]  = timelist

counting.to_csv("Counting sort.csv", index=False)
'''




# 平均資料

counting_avg = hw2_data[0:26]
x_counting = counting_avg["k"].values.reshape(-1,1)
y_counting = counting_avg["Counting sort"].values.reshape(-1,1)

## 訓練資料

counting_train = list()
k_train = list()

for i in range(0,26):
    for j in range(0,10):
        counting_train.append(counting.iloc[j,i])
        k_train.append(hw2_data["k"].iloc[i])

train_dict = {"train_k" : k_train,"train_counting" : counting_train}
train_data = pd.DataFrame(train_dict)


x_counting_train = train_data["train_k"].values.reshape(-1,1)
y_counting_train = train_data["train_counting"].values.reshape(-1,1)

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
  regressor.fit(x_counting_train,y_counting_train)
  ## 裝進精準度
  scores.append(regressor.score(x_counting,y_counting))
  


  ## 預測數據
  pred = regressor.predict(x_counting)
  
  ## 視覺化多項式迴歸模型線
  plt.plot(x_counting, regressor.predict(x_counting), label = 'Polynomial Degree ' + str(polynomial_degree[index]))
      
      
## 印出分數
max_index = scores.index(max(scores))  
print('Polynomial Degree ' + str(max_index+1) + ' Score: ' + str(scores[max_index]))

## 繪製數據集資料點
plt.scatter(x_counting,y_counting)
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
top_regression.fit(x_counting_train,y_counting_train)

## 預測數據
pred_data = regressor.predict(test_data1)

# 儲存預測數據
'''
for i in range(0,30):
    hw2_pred_data["Counting sort"].iloc[i] = pred_data[i][0]   
hw2_pred_data.to_csv("Assignment2_pred_data.csv", index=False)
'''
print(pred_data)


## 視覺化多項式迴歸模型線
plt.style.use("seaborn")
plt.plot(test_data1, regressor.predict(test_data1), color = "red", label = 'Regression Line (polynomial degree '+str(max_index+1)+")")
      
## 繪製數據集資料點
plt.scatter(x_counting,y_counting, color = "orange", label = "Testing average time")
plt.style.use("seaborn")
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.ticklabel_format(style="plain")
plt.title("The Best Regression Line")
plt.legend()
plt.show()

## Time complexity line
x = np.linspace(0, 30, 1000)
y = 2**x+1000
plt.plot(x,y, color = "blue", label = "Time complexity O(n+k)")
plt.style.use("seaborn")
plt.legend()
plt.title("The Time Complexity Line -- Counting Sort")
plt.ticklabel_format(style="plain")
plt.show()


