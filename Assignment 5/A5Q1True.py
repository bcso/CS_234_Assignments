def heapSort(aList):
	"""
	Pre-Condition: aList is a list of any length to be sorted
	Post-Condition: return aList sorted in descending order
	"""
	listLength = len(aList)
	heapList = _heapify(aList, listLength)
	end = listLength - 1

	while end > 0:
		temp = heapList[0]
		heapList[0] = heapList[end]
		heapList[end] = temp
		end = end - 1
		heapList = _siftDown(aList,0, end)
	return heapList

def _heapify(aList, listLength):
	#Start comparison from 2nd element onward for heap building
	end = 1
	while end < listLength:
		#Sift up whenever a new element is added to the heap
		_siftUp(aList, 0 , end)
		end = end + 1
	return aList

def _siftDown(aList, start, end):
	root = start

	#While there is a child
	while root * 2 + 1 <= end:
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

			#
			root = buff
		else:
			return

	return aList

def _siftUp(aList, start, end):
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

##inputList =  [6, 5, 3, 1, 8, 7, 2, 4]
##print(inputList)
##print(heapSort(inputList))

def inserstionSort(aList):
	return None

def insert():
	return None

def pop():
	return None
