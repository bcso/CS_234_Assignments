from A4Q1e import *

def main(testLevel):
	"""
	Pre-conditions: testLevel must be an integer value equal to 1, 2 or 3
	Post-conditions: tests will be carried out to verify the integrity of function implementations for linked lists
	"""

	if (testLevel != 1) and (testLevel != 2) and (testLevel != 3):
		raise ValueError, "Input must be a valid test level integer such as 1, 2 or 3"
	#Create a linked List
	a = LinkedList()
	#Create a normal list
	b = []

	#Make sure empty list is displayed as it should
	if str(b) != str(a):
		raise ValueError, "linked list a is " + str(a) + " expected " + str(b)

	a.append(2.0)
	a.append('good')
	a.append(2)
	a.append('b')
	a.append(True)
	b.append(2.0)
	b.append('good')		
	b.append(2)
	b.append('b')
	b.append(True)

	if testLevel == 1 :		
		if len(a) != 5:
			raise ValueError, "linked list a is length " + str(len(a)) + ", expected length 5"

		if str(b) != str(a):
			raise ValueError, "linked list a is " + str(a) + " expected " + str(b)

		print "All tests passed for test level " + str(testLevel)

	elif testLevel == 2:
		#Remove first value from the linked list
		a.remove(2.0)
		#Remove first value from the normal list
		b.pop(0)
		if len(a) != 4:
			raise ValueError, "linked list a is length " + str(len(a)) + ", expected length 4"

		if str(b) != str(a):
			raise ValueError, "linked list a is " + str(a) + " expected " + str(b)
		
		#Remove last value from linked list
		a.remove(True)
		#Remove last value from the normal list
		b.pop()
		if len(a) != 3:
			raise ValueError, "linked list a is length " + str(len(a)) + ", expected length 3"

		if str(b) != str(a):
			raise ValueError, "linked list a is " + str(a) + " expected " + str(b)

		#Remove second value from linked list
		a.remove(2)
		#Remove second value from the normal list
		b.pop(1)
		if len(a) != 2:
			raise ValueError, "linked list a is length " + str(len(a)) + ", expected length 2"

		if str(b) != str(a):
			raise ValueError, "linked list a is " + str(a) + " expected " + str(b)

		print "All tests passed for test level " + str(testLevel)

	elif testLevel == 3:
		#Pop second value from the linked list
		linkedListPoppedValue = a.pop(1)
		#Pop second value from the normal list
		normalListPoppedValue = b.pop(1)
		if linkedListPoppedValue != 'good':
			raise ValueError, "Popped value of linked list was " + linkedListPoppedValue + " expected " + normalListPoppedValue

		if len(a) != 4:
			raise ValueError, "linked list a is length " + str(len(a)) + ", expected length 4"

		if str(b) != str(a):
			raise ValueError, "linked list a is " + str(a) + " expected " + str(b)

		#Insert removed value to the linked list
		a.insert(1, 'good')
		#Insert removed value to the normal list
		b.insert(1, 'good')
		if len(a) != 5:
			raise ValueError, "linked list a is length " + str(len(a)) + ", expected length 5"

		if str(b) != str(a):
			raise ValueError, "linked list a is " + str(a) + " expected " + str(b)

		#Count occurence of 2 in linked list
		linkedListCountedValue = a.count(2)
		#Count occurence of 2 in normal list
		normalListCountedValue = b.count(2)
		if linkedListCountedValue != 2:
			raise ValueError, "Counted value 2, " + linkedListCountedValue + " times expected " + normalListCountedValue

		print "All tests passed for test level " + str(testLevel)

main(3)