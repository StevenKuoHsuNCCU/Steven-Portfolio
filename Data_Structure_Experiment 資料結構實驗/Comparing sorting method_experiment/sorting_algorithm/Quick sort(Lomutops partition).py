# Quick sort(Lomuto's partition) in Python programming
# https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/


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
	
	# pivot
	pivot = arr[high]
	
	# Index of smaller element
	i = (low - 1)
	for j in range(low, high):
		
		# If current element is smaller than or
		# equal to pivot
		if (arr[j] <= pivot):
			
			# increment index of smaller element
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)
	
''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''

def quickSort(arr, low, high):
	if (low < high):
		
		''' pi is partitioning index, arr[p] is now	
		at right place '''
		pi = partition(arr, low, high)
		
		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)
		
# 輸入 Dataframe
lomuto = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_Lomuto's partition.csv")
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")
hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")



# Experiment
'''
Lomuto = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_Lomuto's partition.csv")    

timelist = list()


for i in range(0,10):
    print(i)
    data = list()
    for j in range(0,2**12):
        data.append(random.randint(1,1000))
    n = len(data)
    start = time.time()
    quickSort(data,0,n-1)
    end = time.time()
    timelist.append(end-start)


Lomuto["k = 12"]  = timelist

Lomuto.to_csv("Quick sort_Lomuto's partition.csv", index=False)
'''

# 平均資料

lomuto_avg = hw2_data[0:23]
x_lomuto = lomuto_avg["k"].values.reshape(-1,1)
y_lomuto = lomuto_avg["Quick sort (Lomuto's partition)"].values.reshape(-1,1)

## 訓練資料

lomuto_train = list()
k_train = list()

for i in range(0,23):
    for j in range(0,10):
        lomuto_train.append(lomuto.iloc[j,i])
        k_train.append(hw2_data["k"].iloc[i])

train_dict = {"train_k" : k_train,"train_lomuto" : lomuto_train}
train_data = pd.DataFrame(train_dict)


x_lomuto_train = train_data["train_k"].values.reshape(-1,1)
y_lomuto_train = train_data["train_lomuto"].values.reshape(-1,1)

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
  regressor.fit(x_lomuto_train,y_lomuto_train)
  ## 裝進精準度
  scores.append(regressor.score(x_lomuto,y_lomuto))
  


  ## 預測數據
  pred = regressor.predict(x_lomuto)
  
  ## 視覺化多項式迴歸模型線
  plt.plot(x_lomuto, regressor.predict(x_lomuto), label = 'Polynomial Degree ' + str(polynomial_degree[index]))
      
      
## 印出分數
max_index = scores.index(max(scores))  
print('Polynomial Degree ' + str(max_index+1) + ' Score: ' + str(scores[max_index]))

## 繪製數據集資料點
plt.scatter(x_lomuto,y_lomuto)
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
top_regression.fit(x_lomuto_train,y_lomuto_train)

## 預測數據
pred_data = regressor.predict(test_data1)

# 儲存預測數據
'''
for i in range(0,30):
    hw2_pred_data["Quick sort (Lomuto's partition)"].iloc[i] = pred_data[i][0]   
hw2_pred_data.to_csv("Assignment2_pred_data.csv", index=False)
'''
print(pred_data)


## 視覺化多項式迴歸模型線
plt.style.use("seaborn")
plt.plot(test_data1, regressor.predict(test_data1), color = "red", label = 'Regression Line (polynomial degree '+str(max_index+1)+")")
      
## 繪製數據集資料點
plt.scatter(x_lomuto,y_lomuto, color = "orange", label = "Testing average time")
plt.style.use("seaborn")
plt.xlabel("2^k data in a unsorted array")
plt.ylabel("time(s)")
plt.ticklabel_format(style="plain")
plt.title("The Best Regression Line")
plt.legend()
plt.show()








# This code is contributed by SHUBHAMSINGH10








