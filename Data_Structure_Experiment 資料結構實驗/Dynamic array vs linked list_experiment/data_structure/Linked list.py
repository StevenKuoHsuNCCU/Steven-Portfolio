from faulthandler import dump_traceback_later
import numpy as np
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
    Saving current time (linked list)
'''

Linked_list_time = SingleLinkedList()
start_time_LL = time.time()

for i in range(1,2**30+1):
    if math.log2(i)%1 == 0:
        print(math.log2(i))
    Linked_list_time.append(time.time())

end_time_LL = time.time()
print("Total spending time:",(end_time_LL - start_time_LL),"s")

'''
	Print the plot (linked list)
'''


Data_time_ll = list()
Data_int_ll = list()
temp = Linked_list_time.head


Data_time_ll.append(0)
for i in range(1,2**30):
    temp = temp.next
    Data_time_ll.append(temp.data-Linked_list_time.head.data)
    
for i in range(1,2**30+1):
    Data_int_ll.append(math.log2(i))


    
    
ll_time_record_df = pd.DataFrame({"Data_amounts":Data_int_ll,"Time":Data_time_ll})

plt.plot(Data_int_ll,Data_time_ll)
plt.show()


















