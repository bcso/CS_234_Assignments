""" test the StringCounts class.

There is not much to test in this class, only one function takes a parameter
"""

from types import StringType
from strCounts import StringCounts

sc = StringCounts()
print ("Test 1: reset an empty object")
sc.reset()

print ("\nTest 2: generate report for an empty object")
print ("Expecting...")
print
print ("Got...")
sc.report()
print ("<EOT> end of test")

sc.add('www.google.ca')
print ("\nTest 3: add to an empty object")
print ("Expecting...")
print ("www.google.ca                                           1")
print ("Got...")
sc.report()
print ("<EOT>")

sc.add('www.google.ca')
print ("\nTest 4: add to an already added string")
print ("Expecting...")
print ("www.google.ca                                           2")
print ("Got...")
sc.report()
print ("<EOT>")

sc.add('www.youtube.com')
print ("\nTest 5: add a new string")
print ("Expecting...")
print ("www.google.ca                                           2")
print ("www.youtube.com                                         1")
print ("Got...")
sc.report()
print ("<EOT>")

sc.reset()
print ("\nTest 6: resetting")
print ("Expecting...")
print
print ("Got...")
sc.report()
print ("<EOT>")

sc.add('www.google.ca')
print ("\nTest 7: add to an reset object")
print ("Expecting...")
print ("www.google.ca                                           1")
print ("Got...")
sc.report()
print ("<EOT>")

try:
   sc.add(1.2)
except TypeError:
   print ("\nTest 8: passed bad input (float)")

try:
   sc.add(1)
except TypeError:
   print ("\nTest 9: passed bad input (int)")

try:
   sc.add(True)
except TypeError:
   print ("\nTest 10: passed bad input (bool)")
