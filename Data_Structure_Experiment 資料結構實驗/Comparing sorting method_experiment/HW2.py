import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split




hw2_pred_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_pred_data.csv")
hw2_data = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Assignment2_data.csv")

#1~18
insertion = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Insertion sort.csv")
#1~26
merge = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Merge sort.csv")
#1~26
counting = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Counting sort.csv")
#1~23
lomuto = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_Lomuto's partition.csv")
#1~27
hoare = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_Hoare's partition.csv")
#1~27
three_way = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 2_1113/Quick sort_3 way partition.csv")


# raw data plot
plt.style.use("seaborn")
hw2_data.plot("k",["Insertion sort","Merge sort","Counting sort","Quick sort (Lomuto's partition)","Quick sort (Hoare's partition)","Quick sort (3 way partition)"])
plt.ticklabel_format(style="plain")
plt.ylim(0,3600)
plt.title("Experiment data")
plt.legend()
plt.show()

# raw prediction data
plt.style.use("seaborn")
hw2_pred_data.plot("k",["Insertion sort","Merge sort","Counting sort","Quick sort (Lomuto's partition)","Quick sort (Hoare's partition)","Quick sort (3 way partition)"])
plt.ticklabel_format(style="plain")
plt.title("Prediction data")
plt.ylim(0,3600)
plt.legend()
plt.show()

# raw prediction data (without the top 2)
plt.style.use("seaborn")
hw2_pred_data.plot("k",["Merge sort","Counting sort","Quick sort (Hoare's partition)","Quick sort (3 way partition)"])
plt.ticklabel_format(style="plain")
plt.legend()
plt.ylim(0,3600)
plt.title("Prediction data")
plt.show()




# raw data with units
plt.style.use("seaborn")
hw2_data.plot("units",["Insertion sort","Merge sort","Counting sort","Quick sort (Lomuto's partition)","Quick sort (Hoare's partition)","Quick sort (3 way partition)"])
plt.ticklabel_format(style="plain")
plt.title("Experiment Data")
plt.legend()
plt.show()



# time complexity plot
x1 = np.linspace(0, 2**30, 1000)
y1 = x1**2
plt.plot(x1,y1, color = "blue", label = "Time complexity O(n-square)")
x2 = np.linspace(0, 2**30, 1000)
y2 = x2*np.log2(x2)
plt.plot(x2,y2, color = "red", label = "Time complexity O(nlogn)")
x3 = np.linspace(0, 2**30, 1000)
y3 = x3+1000
x4 = np.linspace(0, 2**30, 1000)
y4 = x4*np.log2(x4)*9
plt.plot(x4,y4, color = "blue", label = "Time complexity O(9nlogn)")
plt.plot(x3,y3, color = "orange", label = "Time complexity O(n+k)")
plt.style.use("seaborn")
plt.title("The Time Complexity Line")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()


# time complexity plot (without n^2)

x2 = np.linspace(0, 2**30, 1000)
y2 = x2*np.log2(x2)
plt.plot(x2,y2, color = "red", label = "Time complexity O(nlogn)")
x3 = np.linspace(0, 2**30, 1000)
y3 = x3+1000
plt.plot(x3,y3, color = "orange", label = "Time complexity O(n+k)")
x4 = np.linspace(0, 2**30, 1000)
y4 = x4*np.log2(x4)*9
plt.plot(x4,y4, color = "blue", label = "Time complexity O(9nlogn)")
plt.style.use("seaborn")
plt.title("The Time Complexity Line")
plt.legend()
plt.ticklabel_format(style="plain")
plt.show()

