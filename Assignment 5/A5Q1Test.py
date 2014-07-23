"""
A5 Q1 Testing

This file will run the implementations of heapSort and insertionSort, whilst comparing the results 
with the built-in python sorting function.

"""
#Import random generation tools
from random import seed, randint

#(Required) Import the sorting function implementations to be tested for
from A5Q1 import heapSort, insertionSort

#This is the maximum acceptable integer that will appear in the generated lists
MAX_INT = 2147483647

def testHeapSort(aSeed):
	seed(aSeed)

	#Start with list size 4
	listSize = 4
	
	#listSize will increase as follows: 4, 16, 64, 256, 1024
	while listSize <= 2000:
		baseList = []

		#Generate the list of random ints
		for i in range(listSize):
			baseList.append(randint(0,MAX_INT))

		#Test python sort
		pythonSortList = baseList[:]
		pythonSortList.sort(reverse=True)
		print pythonSortList

		#Test heap sort
		heapSortList = baseList[:]
		heapSort(heapSortList)
		print heapSortList		

		#Test insertion sort
		insertionSortList = baseList[:]
		insertionSort(insertionSortList)
		print insertionSortList
		
		assert pythonSortList == heapSortList
		assert pythonSortList == insertionSortList
		listSize = listSize*4

#Run the test
testHeapSort(3434)
