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


ll = 0
hh = 0

def partition_l(arr, low, high,ll):
	
	# pivot
	pivot = arr[high]
	ii += 1
	# Index of smaller element
	i = (low - 1)
	for j in range(low, high):
		
		# If current element is smaller than or
		# equal to pivot
		if (arr[j] <= pivot):
			ll +=1
			# increment index of smaller element
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)
	
''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''

def quickSort_l(arr, low, high):
	if (low < high):
		
		''' pi is partitioning index, arr[p] is now	
		at right place '''
		pi = partition_l(arr, low, high)
		
		# Separately sort elements before
		# partition and after partition
		quickSort_l(arr, low, pi - 1)
		quickSort_l(arr, pi + 1, high)
  
  
  
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
		ll += 1
  
  
  
  


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
  
  
  
lll = list()
hhh = list()

for i in range(1,2):
    dd = list()
    ee = list()
    ee = dd
    for j in range(0,2**i):
        dd.append(random.randint(1,1000))
    quickSort_l(dd,0,len(dd)-1)
    quickSort(ee,0,len(ee)-1)
    print(e,)


