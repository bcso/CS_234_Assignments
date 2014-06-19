"""CS 234 Assignment 3 Question 2c

This is a testing file to test strCounts.py
"""


def getValue(anHTTPmsg, paramName):
	"""
	Pre-conditions: 
		anHTTPmsg and paramName must be string types
		anHTTPmsg and paramName cannot be empty
	Post-conditions:
		return a string that is the value of paramName, found in anHTTPmsg

	getValue will search an input string, anHTTPmsg and return the value associated with the parameter paramName in it.
	"""

	
	if type(anHTTPmsg) != type("s"):
		raise TypeError, "anHTTPmsg must be a string!"
	elif len(anHTTPmsg) == 0:
		raise ValueError, "anHTTPmsg cannot be empty!"
	elif type(paramName) != type("s"):
		raise TypeError, "paramName must be a string!"
	elif len(paramName) == 0:
		raise ValueError, "paramName cannot be empty!"

	#Instantiate the final value string older
	finalValue = ""

	#Split the message input into list of lines (as strings)
	lines = anHTTPmsg.splitlines()

	#Loop through each line
	for line in lines:
		#Split each line into list of words
		wordsList = line.split()
		#Retrieve the first word of each line as the param
		param = wordsList[0]
		#Check if the param is the one we need to match
		if param == paramName:
			#Loop through each word in the line, past the first letter to get the value
			for value in wordsList[1:]:
				finalValue += (value + " ")

	#Remove last whitespace
	return finalValue[:-1]
			
def hasParam(anHTTPmsg, paramName):
	"""
	Pre-conditions: 
		anHTTPmsg and paramName must be string types
		anHTTPmsg and paramName cannot be empty
	Post-conditions:
		return boolean value for paramName exists in anHTTPmsg, but also must be in acceptedParams

	hasParam returns the boolean value for whether or not paramName exists in anHTTPmsg as a parameter, and 
	must also be in acceptedParams
	"""

	if type(anHTTPmsg) != type("s"):
		raise TypeError, "anHTTPmsg must be a string!"
	elif len(anHTTPmsg) == 0:
		raise ValueError, "anHTTPmsg cannot be empty!"
	elif type(paramName) != type("s"):
		raise TypeError, "paramName must be a string!"
	elif len(paramName) == 0:
		raise ValueError, "paramName cannot be empty!"

	#Split the message input into list of lines (as strings)
	lines = anHTTPmsg.splitlines()

	#This checks for false or true for matching param in anHTTPmsg to paramName
	exists = False

	#These are valid params
	acceptedParams = ["Host:", "User-Agent:", "Accept:", "Accept-Language:"]

	#Loop through each line
	for line in lines:
		#Split each line into list of words
		wordsList = line.split()
		#Retrieve the first word of each line as the param
		param = wordsList[0]
		#Check if the param is the one we need to match
		if (param == paramName) and (param in acceptedParams):
			exists = True

	return exists