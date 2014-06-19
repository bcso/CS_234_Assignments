"""CS 234 Assignment 3 Question 2d

This is a testing file to test strCommands.py
"""

from strCommands import *

aCorrectMsg = """GET http://www.lib.uwaterloo.ca/hours/ HTTP/1.1
Host: www.lib.uwaterloo.ca
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive"""

assert getValue(aCorrectMsg, "User-Agent:") == "Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0"

assert hasParam(aCorrectMsg, "User-Agent:") == True

anIncorrectMsg = """GET http://www.lib.uwaterloo.ca/hours/ HTTP/1.1
Host: www.lib.uwaterloo.ca
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: I_Lay_Cookies"""

assert getValue(anIncorrectMsg, "Cookie:") == "I_Lay_Cookies"

assert hasParam(anIncorrectMsg, "Cookie:") == False

print ("All tests have passed.")