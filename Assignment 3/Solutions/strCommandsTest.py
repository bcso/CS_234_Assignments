""" test the string command functions
"""

from types import StringType
from strCommands import hasParam, getValue
from HTTP_examples import msg1

#
# Test for bad input, but always give a valid http msg
#

try:
   getValue(msg1, 1)
except TypeError:
   print("Passed 1 - detect type error in 2nd param")

try:
   getValue(msg1, "")
except ValueError:
   print("Passed 2 - detect a blank string as 2nd param")

try:
   getValue(msg1, "Host")
except ValueError:
   print("Passed 3 - detect a 2nd param without a colon")

try:
   hasParam(msg1, 1)
except TypeError:
   print("Passed 4 - detect type error in 2nd param")

try:
   hasParam(msg1, "")
except ValueError:
   print("Passed 5 - detect a blank string as 2nd param")

try:
   hasParam(msg1, "Host")
except ValueError:
   print("Passed 6 - detect a 2nd param without a colon")

#
# Test for good input,
#

# try 3 positions of parameters: beginning, middle, end

if hasParam(msg1, "Host:"):
   print ("Passed 7 - detect 1st HTTP parameter")

if hasParam(msg1, "Accept:"):
   print ("Passed 8 - detect a middle HTTP parameter")

if hasParam(msg1, "Connection:"):
   print ("Passed 9 - detect last HTTP parameter")


if getValue(msg1, "Host:")== "www.lib.uwaterloo.ca":
   print ("Passed 10 - get 1st HTTP parameter value")

if getValue(msg1, "Accept:") == \
   "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8":
   print ("Passed 11 - get a middle HTTP parameter value")

if getValue(msg1, "Connection:") == "keep-alive":
   print ("Passed 12 - get last HTTP parameter value")


# try parameter that is not in the HTTP msg


if not hasParam(msg1, "Cookie:"): 
   print ("Passed 13 - a param that is not in the HTTP msg")

try:
   getValue(msg1, "Cookie:")
except ValueError:
   print ("Passed 14 - ask for value of a param that is not in the HTTP msg")   


