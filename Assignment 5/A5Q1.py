"""
A5 Q1 Main Sorting  function file

This file contains all the required functions to run heapSort and insertionSort

"""

def heapSort(aList):
	"""
	Pre-Condition: aList is a list of any length to be sorted
	Post-Condition: return aList sorted in descending order
	"""
	listLength = len(aList)
	_heapify(aList, listLength)
	end = listLength - 1

	#Decrease the value of end upon each loop,
	#since the latest last value will be in sorted position
	while end > 0:		
		temp = aList[0]
		aList[0] = aList[end]
		aList[end] = temp				
		end = end - 1
		##The heap is out of order now, need to sift it back to proper order
		_siftDown(aList,0, end)

def _heapify(aList, listLength):
	"""
	Pre-Condition: listLength must be the total length of the provided list (aList)
	Post-Condition: will turn aList into a sorted heap for use in sorting in descending order
	"""
	#Start comparison from 2nd element onward for heap building
	end = 1
	while end < listLength:
		#Sift up whenever a new element is added to the heap
		_siftUp(aList, 0 , end)
		end = end + 1

def _siftDown(aList, start, end):
	"""
	Pre-Condition: start, end positions must exist
	Post-Condition: aList will be have parents smaller than children 
	"""

	root = start

	#While there is a child
	while (root * 2 + 1) <= end:
		#keep track of the child
		child = root * 2 + 1
		#Keep track of the root
		buff = root

		#Check for left child
		if aList[buff] > aList[child]:
			buff = child

		#Check for a right child
		if child + 1 <= end and aList[buff] > aList[child + 1]:
			buff = child + 1

		#There is a value that needs to be swapped with aList[buff] and aList[root]
		if buff != root:
			#Swap the root and last element
			temp = aList[root]
			aList[root] = aList[buff]
			aList[buff] = temp
			#Move down a node
			root = buff
		else:
			return

def _siftUp(aList, start, end):
	"""
	Pre-Condition: start, end positions must exist
	Post-Condition: aList will be have parents smaller than children 
	"""	
	child = end
	#Do this while we are not at the root
	while child > start:
		parent = (child - 1)//2
		#If parent is larger than child...
		if (aList[parent] > aList[child]):
			#We commence the swap
			temp = aList[parent]
			aList[parent] = aList[child]
			aList[child] = temp
			#Move up a level
			child = parent
		else:
			return

def insertionSort(aList):
	"""
	Pre-Condition: aList must be a list of integers
	Post-Condition: aList will be sorted in descending order
	"""

	#starting from 1, compare values going from left to right, up to the lenght of the list
	for i in range(1,len(aList)):
		j = i
		while j > 0 and aList[j-1] < aList[j]:
			temp = aList.pop(j-1)
			aList.insert(j, temp)
			j -= 1

