"""CS 234 Assignment 3 Question 2b

This is a testing file to test strCounts.py
"""

from strCounts import *

sdict = StringCounts()
sdict.add("testString1")
assert len(sdict._stringDict) == 1
assert sdict._stringDict["testString1"] == 1

sdict.add("testString1")
assert len(sdict._stringDict) == 1
assert sdict._stringDict["testString1"] == 2

sdict.add("testString2")
assert len(sdict._stringDict) == 2
assert sdict._stringDict["testString1"] == 2
assert sdict._stringDict["testString2"] == 1

sdict.add("testString2")
assert len(sdict._stringDict) == 2
assert sdict._stringDict["testString1"] == 2
assert sdict._stringDict["testString2"] == 2

sdict.report()
sdict.reset()

assert len(sdict._stringDict) == 0

print ("All tests have passed.")
