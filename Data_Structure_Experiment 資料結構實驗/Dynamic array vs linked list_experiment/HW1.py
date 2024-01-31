from ast import Index
from faulthandler import dump_traceback_later
from turtle import st
import numpy as np
np.set_printoptions(suppress=True)
import sys
import ctypes as c
import random as rd
import time
import pandas as pd
import matplotlib.pyplot as plt
import math
import psutil
import os
from pympler.tracker import SummaryTracker
import gc
import csv
from decimal import Decimal

pd.set_option('float_format', lambda x: '%.6f' % x)
'''
	Time list
'''
dyarr_tra_logn =list()
dyarr_sum_logn =list()
dyarr_tra_n =list()
dyarr_sum_n =list()

ll_tra_logn =list()
ll_sum_logn =list()
ll_tra_n =list()
ll_sum_n =list()




'''
Dynamic array reference

https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/
'''

class DynamicArray(object):
	'''
	DYNAMIC ARRAY CLASS (Similar to Python List)
	'''
	
	def __init__(self):
		self.n = 0 # Count actual elements (Default is 0)
		self.capacity = 1 # Default Capacity
		self.A = self.make_array(self.capacity)


		
	def __len__(self):
		"""
		Return number of elements sorted in array
		"""
		return self.n
	
	def __getitem__(self, k):
		"""
		Return element at index k
		"""
		if not 0 <= k <self.n:
			# Check it k index is in bounds of array
			return IndexError('K is out of bounds !')
		
		return self.A[k] # Retrieve from the array at index k
		
	def append(self, ele):
		"""
		Add element to end of the array
		"""
		if self.n == self.capacity:
      
			# Double capacity if not enough room
			self._resize(2 * self.capacity)
			
		
		self.A[self.n] = ele # Set self.n index to element
		self.n += 1

	
		
	def _resize(self, new_cap):
		"""
		Resize internal array to capacity new_cap
		"""
		B = self.make_array(new_cap) # New bigger array
  
    
		for k in range(self.n): # Reference all existing values
			B[k] = self.A[k]
   
  
		del self.A
		self.A = B # Call A the new bigger array
		self.capacity = new_cap    # Reset the capacity
  
		
  

    
		
	def make_array(self, new_cap):
		"""
		Returns a new array with new_cap capacity
		"""
		return (new_cap*c.py_object)()



'''
Linked list reference

https://lovedrinkcafe.com/python-single-linked-list/
'''


class Node:
    def __init__(self ,data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        

        else:
            self.tail.next = new_node
            self.tail = self.tail.next
       
       
       
            
            
    def delete(self):
        if self.head == None:
            return print("This list is empty")
        else:
            if len(self) == 1:
                self.head = None
            else:
                current_node = self.head
                while current_node.next != None:
                    self.tail = current_node
                    current_node = current_node.next
                self.tail.next = None
                
    def insert(self, index , data):
        '''
        To insert the data to the specific index
        '''
        if self.head == None:
            print("You can only insert the data to a not empty list")
        if not 1 <= index <= len(self):
            print("{} is not in range".format(index))

        elif index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            cur_idx = 1
            new_node = Node(data)
            current_node = self.head
            while cur_idx+1 != index:
                current_node = current_node.next
                cur_idx += 1
            new_node.next = current_node.next
            current_node.next = new_node
    def delete_node_by_index(self, index):
        '''
        To delete the specific node
        '''
        if self.head == None:
            print("You can only delete the data from a not empty list")

        if index == 1 and len(self) > 1:
            self.head = self.head.next

        elif index == 1 and len(self) == 1:
            self.head = None
            self.tail = None

        elif 1 < index < len(self):
            cur_idx = 1
            current_node = self.head
            while cur_idx != index:
                previous_node = current_node
                current_node = current_node.next
                cur_idx += 1
            previous_node.next = current_node.next
            
        elif index == len(self):
            cur_idx = 1
            current_node = self.head
            while cur_idx != index:
                previous_node = current_node
                current_node = current_node.next
                cur_idx += 1
            previous_node.next = None
            self.tail = previous_node

        else:
            print("index out of range")
            
    def reverse(self):

        # reverse the order of the list
        previous_node = None
        current_node = self.head
        self.tail = current_node
        next_node = current_node.next

        while next_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = previous_node
        self.head = current_node
        return


    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length
    
    def __str__(self):
        current_node = self.head
        chain = []
        index = 1
        while current_node != None:
            chain.append("["+str(index)+"]"+str(current_node.data))
            index += 1
            current_node = current_node.next
        return " --> ".join(chain)


'''
	Read csv
'''
sum = pd.read_csv("25sum.csv")
store = pd.read_csv("25store.csv")


'''
	Experiment


#Dynamic array (store)
DyArr_time = DynamicArray()
start_time_DA = time.time()

for i in range(1,2**25+1):
    DyArr_time.append(time.time())
    
end_time_DA = time.time()
print("Dynamic array tranversing total spending time:",(end_time_DA - start_time_DA),"s")

for i in range(0,2**25):
    dyarr_tra_n.append(Decimal(DyArr_time[i]-DyArr_time[0]))
    

store["Dynamic array store"] = dyarr_tra_n
print(store)
store.to_csv("25store.csv")
'''
'''
#Dynamic array (sum)
 
dyarr_sum = 0
start_time_dasum = time.time()
for i in range(0,2**26):
    dyarr_sum = DyArr_time[i]+dyarr_sum
    dyarr_sum_n.append(time.time()- start_time_dasum)
    if math.log2(i+1)%1 ==0:
        dyarr_sum_logn.append(time.time()-start_time_dasum)
        
end_time_dasum = time.time()

n["Dynamic array sum"] = dyarr_sum_n
n.to_csv("dyna ll n.csv")

print(len(dyarr_sum_n))
print("Dynamic array addition total time",end_time_dasum - start_time_dasum,"s")












'''


#Linked list (store)
Linked_list_time = SingleLinkedList()
start_time_LL = time.time()

for i in range(1,2**25+1):
    Linked_list_time.append(time.time())
    
end_time_LL = time.time()
print("Linked list tranversing total spending time:",(end_time_LL - start_time_LL),"s")

k = Linked_list_time.head
ll_tra_n.append(0)
for i in range(1,2**25):
    k = k.next
    temp = k.data-Linked_list_time.head.data
    ll_tra_n.append(temp)
    



store["Linked list store"] = ll_tra_n



print(store)
store.to_csv("25store.csv")

'''


#Linked list (Sum)
ll_sum = Linked_list_time.head.data
temp = Linked_list_time.head
ll_sum_n.append(0)
start_time_llsum = time.time()
for i in range(1,2**26):
    ll_sum_n.append(time.time()-start_time_llsum)
    temp = temp.next
    ll_sum = ll_sum + temp.data
    if math.log2(i)%1 ==0:
        ll_sum_logn.append(time.time()-start_time_llsum)
end_time_llsum = time.time()
ll_sum_logn.append(end_time_llsum - start_time_llsum)
n["Linked list sum"] = ll_sum_n
print(len(ll_sum_n))
print("Linked list addition total time",end_time_llsum - start_time_llsum,"s")
n.to_csv("dyna ll n.csv")
'''




'''
	Print the plot (dynamic array)



#dyarr vs linked list (traverse)

vs_tra = logk_csv[["Dynamic array store","Linked list store"]]
vs_tra.plot(xlabel="log N",ylabel="t(s)")
plt.show()

#dyarr vs linked list (traverse)

vs_sum = logk_csv[["Dynamic array sum","Linked list sum"]]

vs_sum.plot(xlabel="log N",ylabel="t(s)")
plt.show()
'''




'''
    see the size


a = DynamicArray()
a.append(time.time())
print(sys.getsizeof(a[0]))



b = SingleLinkedList()
b.append(time.time())
b.append(time.time())
print(sys.getsizeof(b.head.data))
print(sys.getsizeof(b.head.next))

'''














