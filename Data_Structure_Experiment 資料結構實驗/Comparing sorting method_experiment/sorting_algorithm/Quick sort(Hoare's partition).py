# Quick sort(Hoare's partition) in Python programming
# https://www.geeksforgeeks.org/hoares-vs-hoare-partition-scheme-quicksort/


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



def partition(arr, low, high):

	pivot = arr[low]
	i = low - 1
	j = high + 1

	while (True):

		# Find leftmost element greater than
		# or equal to pivot
		i += 1
		while (arr[i] < pivot):
			i += 1

		# Find rightmost element smaller than
		# or equal to pivot
		j -= 1
		while (arr[j] > pivot):
			j -= 1

		# If two pointers met.
		if (i >= j):
			return j

		arr[i], arr[j] = arr[j], arr[i]


''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''


def quickSort(arr, low, high):
	''' pi is partitioning index, arr[p] is now
	at right place '''
	if (low < high):

		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi)
		quickSort(arr, pi + 1, high)


''' Function to print an array '''

# 輸入 Dataframe
hoare = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_Hoare's partition.csv")
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")
hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")


# Experiment
'''
Hoare = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_Hoare's partition.csv")    

timelist = list()


for i in range(0,10):
    print(i)
    data = list()
    for j in range(0,2**14):
        data.append(random.randint(1,1000))
    n = len(data)
    start = time.time()
    quickSort(data,0,n-1)
    end = time.time()
    timelist.append(end-start)


Hoare["k = 14"]  = timelist

Hoare.to_csv("Quick sort_Hoare's partition.csv", index=False)
'''

# 平均資料

hoare_avg = hw2_data[0:27]
x_hoare = hoare_avg["k"].values.reshape(-1,1)
y_hoare = hoare_avg["Quick sort (Hoare's partition)"].values.reshape(-1,1)

## 訓練資料

hoare_train = list()
k_train = list()

for i in range(0,27):
    for j in range(0,10):
        hoare_train.append(hoare.iloc[j,i])
        k_train.append(hw2_data["k"].iloc[i])

train_dict = {"train_k" : k_train,"train_hoare" : hoare_train}
train_data = pd.DataFrame(train_dict)


x_hoare_train = train_data["train_k"].values.reshape(-1,1)
y_hoare_train = train_data["train_hoare"].values.reshape(-1,1)

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
  regressor.fit(x_hoare_train,y_hoare_train)
  ## 裝進精準度
  scores.append(regressor.score(x_hoare,y_hoare))
  


  ## 預測數據
  pred = regressor.predict(x_hoare)
  
  ## 視覺化多項式迴歸模型線
  plt.plot(x_hoare, regressor.predict(x_hoare), label = 'Polynomial Degree ' + str(polynomial_degree[index]))
      
      
## 印出分數
max_index = scores.index(max(scores))  
print('Polynomial Degree ' + str(max_index+1) + ' Score: ' + str(scores[max_index]))

## 繪製數據集資料點
plt.scatter(x_hoare,y_hoare)
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
top_regression.fit(x_hoare_train,y_hoare_train)

## 預測數據
pred_data = regressor.predict(test_data1)

# 儲存預測數據
'''
for i in range(0,30):
    hw2_pred_data["Quick sort (Hoare's partition)"].iloc[i] = pred_data[i][0]   
hw2_pred_data.to_csv("Assignment2_pred_data.csv", index=False)
'''
print(pred_data)


## 視覺化多項式迴歸模型線
plt.style.use("seaborn")
plt.plot(test_data1, regressor.predict(test_data1), color = "red", label = 'Regression Line (polynomial degree '+str(max_index+1)+")")
      
## 繪製數據集資料點
plt.scatter(x_hoare,y_hoare, color = "orange", label = "Testing average time")
plt.style.use("seaborn")
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.ticklabel_format(style="plain")
plt.title("The Best Regression Line")
plt.legend()
plt.show()




# This code is contributed by shubhamsingh10
