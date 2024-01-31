# Skip List Implementattion
# SourceCode : https://www.geeksforgeeks.org/skip-list-set-2-insertion/

# k = 23 (記憶體不足)


import treap
import random
import pandas as pd
import numpy as np
import time


"""************************************************************* Source Code ******************************************************************"""


# Python3 code for searching and deleting element in skip list

import random

class Node(object):
	'''
	Class to implement node
	'''
	def __init__(self, key, level):
		self.key = key

		# list to hold references to node of different level
		self.forward = [None]*(level+1)

class SkipList(object):
	'''
	Class for Skip list
	'''
	def __init__(self, max_lvl, P):
		# Maximum level for this skip list
		self.MAXLVL = max_lvl

		# P is the fraction of the nodes with level
		# i references also having level i+1 references
		self.P = P

		# create header node and initialize key to -1
		self.header = self.createNode(self.MAXLVL, -1)

		# current level of skip list
		self.level = 0
	
	# create new node
	def createNode(self, lvl, key):
		n = Node(key, lvl)
		return n
	
	# create random level for node
	def randomLevel(self):
		lvl = 0
		while random.random()<self.P and \
			lvl<self.MAXLVL:lvl += 1
		return lvl

	# insert given key in skip list
	def insertElement(self, key):
		# create update array and initialize it
		update = [None]*(self.MAXLVL+1)
		current = self.header

		'''
		start from highest level of skip list
		move the current reference forward while key
		is greater than key of node next to current
		Otherwise inserted current in update and
		move one level down and continue search
		'''
		for i in range(self.level, -1, -1):
			while current.forward[i] and \
				current.forward[i].key < key:
				current = current.forward[i]
			update[i] = current

		'''
		reached level 0 and forward reference to
		right, which is desired position to
		insert key.
		'''
		current = current.forward[0]

		'''
		if current is NULL that means we have reached
		to end of the level or current's key is not equal
		to key to insert that means we have to insert
		node between update[0] and current node
	'''
		if current == None or current.key != key:
			# Generate a random level for node
			rlevel = self.randomLevel()

			'''
			If random level is greater than list's current
			level (node with highest level inserted in
			list so far), initialize update value with reference
			to header for further use
			'''
			if rlevel > self.level:
				for i in range(self.level+1, rlevel+1):
					update[i] = self.header
				self.level = rlevel

			# create new node with random level generated
			n = self.createNode(rlevel, key)

			# insert node by rearranging references
			for i in range(rlevel+1):
				n.forward[i] = update[i].forward[i]
				update[i].forward[i] = n

		

	def deleteElement(self, search_key):

		# create update array and initialize it
		update = [None]*(self.MAXLVL+1)
		current = self.header

		'''
		start from highest level of skip list
		move the current reference forward while key
		is greater than key of node next to current
		Otherwise inserted current in update and
		move one level down and continue search
		'''
		for i in range(self.level, -1, -1):
			while(current.forward[i] and \
				current.forward[i].key < search_key):
				current = current.forward[i]
			update[i] = current

		'''
		reached level 0 and advance reference to
		right, which is possibly our desired node
		'''
		current = current.forward[0]

		# If current node is target node
		if current != None and current.key == search_key:

			'''
			start from lowest level and rearrange references
			just like we do in singly linked list
			to remove target node
			'''
			for i in range(self.level+1):

				'''
				If at level i, next node is not target
				node, break the loop, no need to move
				further level
				'''
				if update[i].forward[i] != current:
					break
				update[i].forward[i] = current.forward[i]

			# Remove levels having no elements
			while(self.level>0 and\
				self.header.forward[self.level] == None):
				self.level -= 1
			print("Successfully deleted {}".format(search_key))

	def searchElement(self, key):
		current = self.header

		'''
		start from highest level of skip list
		move the current reference forward while key
		is greater than key of node next to current
		Otherwise inserted current in update and
		move one level down and continue search
		'''
		for i in range(self.level, -1, -1):
			while(current.forward[i] and\
				current.forward[i].key < key):
				current = current.forward[i]

		# reached level 0 and advance reference to
		# right, which is possibly our desired node
		current = current.forward[0]

		# If current node have key equal to
		# search key, we have found our target node
		


	# Display skip list level wise
	def displayList(self):
		print("\n*****Skip List******")
		head = self.header
		for lvl in range(self.level+1):
			print("Level {}: ".format(lvl), end=" ")
			node = head.forward[lvl]
			while(node != None):
				print(node.key, end=" ")
				node = node.forward[lvl]
			print("")





"""************************************************************* Import dataframe ******************************************************************"""

add = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_add_data.csv")

search = pd.read_csv("/Users/stevenkuo/College Course/大二/Data Structure/Assignment 3_1225/HW3_search_data.csv")



"""************************************************************* Experiment add ******************************************************************"""

#test variable
x = 24


lst = SkipList(x+3, 0.5)


start_add = time.time()

for i in range(0,2**x):
    lst.insertElement(random.randint(1,2**30+1))
    
end_add = time.time()

add_time =  end_add - start_add
add["Skip List"].iloc[x-15] = add_time






"""************************************************************* Experiment (search) ******************************************************************"""

start_search = time.time()

for i in range(0,100000):
	lst.searchElement(random.randint(1,2**30+1))
    
end_search = time.time()
    
search_time = (end_search - start_search)
search["Skip List"].iloc[x-15] = search_time


print("add time:",add_time)
print("search time:",search_time)


"""************************************************************* Save data ******************************************************************"""

add.to_csv("HW3_add_data.csv", index=False)
search.to_csv("HW3_search_data.csv", index=False)







