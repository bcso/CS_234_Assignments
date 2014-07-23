"""
A5 Q1 Run time testing

Have this file is the same directory as A5Q1.py then run it.

"""

from random import seed, randint
from time import clock
MAX_INT = 2147483647


#
# you must provide this file (A5Q1.py) and these functions
#
from A5Q1 import heapSort, insertionSort


def main(aSeed):
   """ report the timing for 3 different sorts
       aSeed is a positive integer
   """

   seed(aSeed)    # sets up the random number generator

   # print the column headings for the results table
   #
   print("%7s %10s  %10s  %10s" % ("Size" , "Python Srt", "HeapSort",\
                                   "Insert Srt"))

   #
   # create lists of size 4, 16, 64, 246, 1024, 4096, 16384
   # with random integers in them
   #
   listSize = 4
   list = []
   while listSize <= 20000:
      for i in range(listSize):
         list.append(randint(0, MAX_INT))

      #
      # Time how long it takes to sort the list
      #

      # make a copy of list for each sort so they all
      # get the same list

      #first with Python's sort
      listToSort = list[:]
      startTime = clock()
      listToSort.sort(reverse=True)
      endTime = clock()
      pSort = endTime-startTime

      #next with heapsort
      listToSort = list[:]
      startTime = clock()
      print(listToSort)
      heapSort(listToSort)
      endTime = clock()
      hSort = endTime-startTime

      #finally with insertionSort
      # listToSort = list[:]
      # startTime = clock()
      # insertionSort(listToSort)
      # endTime = clock()
      iSort = endTime-startTime

      #print out the results
      print("%7d %10.6f  %10.6f  %10.6f" % (listSize, pSort, hSort, iSort))
      listSize = listSize * 4      



# the if __name__ == "__main__" condition means do the 
# statements below if I run the script but not if I import it
if __name__ == "__main__":
   main(3434)

