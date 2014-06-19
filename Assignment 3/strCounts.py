"""CS 234 Assignment 3 Question 2a

This class initiates an object that keeps track of strings, and how many times they have appeared.
"""
class StringCounts:

	def __init__(self):
		"""
		This is the constructor, a dictionary is created
		"""
		self._stringDict = {}

	def add(self, aString):
		"""
		Pre-conditions: aString must be a string variable
		Post-conditions: the variable will be stored in the StringCounts variable for reference

		Creates an entry in the _stringDict dictionary if it does not contain the string
		else it will increment the count of the string up by one if it already exists.
		"""

		#Raise errors accordingly
		if type(aString) != type("a"):
			raise TypeError, "Input string must be a string type!"
		elif len(aString) == 0:
			raise ValueError, "Input string cannot be empty!"

		#Check if the string does not exist in the dictionary
		if self._stringDict.get(aString) == None:
			#Initiate the string key, assign count to one
			self._stringDict[aString] = 1

		#Check if the string already exists in the dictionary
		elif self._stringDict[aString] != None:
			#Increment the string count by 1 up
			self._stringDict[aString] += 1

	def report(self):
		"""
		Post-conditions: Print out all the strings that have been added, along with their counts

		Report the dictionary of all string values and accumulated counts in a friendly format to the user.
		"""	

		#Loop through the dictionary for keys and values
		for key, value in self._stringDict.iteritems():
			#Print the keys and values in an organized manner
			print ("%-50s %4d") %(key, value)

	def reset(self):
		"""
		Post-conditions: remove all strings and counts from the object

		Reset the self._stringDict variable.
		"""

		self._stringDict = {}

