from types import StringType

class StringCounts(object):
   """Keep track of how many times a string has been added to the object
   """

   def __init__(self):
      """
      Postconditions: create an empty StringCounts object
      """
      self._counts = {}


   def add(self, aString):
      """
      Precondition: aString must be a string type
      Postcondition: increase the count associated with aString by 1
      """
      if type(aString) != StringType:
         raise TypeError, "in add, expecting a string, got " + \
         str(aString)
      if aString in self._counts:
         self._counts[aString] += 1
      else:
         self._counts[aString] = 1
        

   def reset(self):
      """
      Postcondition: erase all strings and counts
      """
      self._counts = {}  
        

   def report(self):
      """
      Postcondition: print out all the strings and counts
      stored in this object
      """
      if self._counts == {}:
         print
      for k in self._counts.keys():
         print("%-50s   %4d" % (k, self._counts[k]))
