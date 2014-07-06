from types import StringType

#
# factor out this common function
#

def _getVal(anHTTPmsg, paramName):
   """ postcondition: return the param value associated with paramName
       or raise a ValueError if anHTTPmsg does not contain paramName
       assume: function parameters have already been checked
   """
   try:
      for line in anHTTPmsg.splitlines():
         if len(line) > len(paramName):
            if line[:len(paramName)] == paramName:
               if line[len(paramName)] == ' ':
                  return line[len(paramName)+1:]
      raise ValueError, "cannot find paramName"
   except Exception:
      raise ValueError, "cannot find paramName"

def getValue(anHTTPmsg, paramName):
   """ preconditions:
       - both parameters are strings
       - the second parametr ends in a colon
       postconditions:  return the param value associated with paramName 
         or raises a ValueError if anHTTPmsg does not contain paramName
       assume: anHTTPmsg is a valid HTTP message
   """
   #
   # test preconditions
   #
   if type(anHTTPmsg) != StringType:
      raise TypeError, "in getValue, expecting a string for " + \
            "the first parameter, got " + str(paramName)
   if type(paramName) != StringType:
      raise TypeError, "in getValue, expecting a string for " + \
            "the second parameter, got " + str(paramName)
   if paramName == '':
      raise ValueError, "in getValue, the second parameter " + \
            "cannot be an empty string"
   if paramName[-1] != ':':
      raise ValueError, "in getValue, expecting the second parameter " + \
            "to end with a ':', got " + str(paramName)
   try:
      return _getVal(anHTTPmsg, paramName)
   except ValueError:
      raise ValueError, "cannot find host in HTTP message"


def hasParam(anHTTPmsg, paramName):
   """ preconditions:
       - both parameters are strings
       - the second parameter ends in a colon
       postconditions:return True if paramName is a parameter name in 
         anHTTPmsg else return False
       assume: anHTTPmsg is a valid HTTP message
   """
   if type(anHTTPmsg) != StringType:
      raise TypeError, "in getValue, expecting a string for " + \
            "the first parameter, got " + str(paramName)
   if type(paramName) != StringType:
      raise TypeError, "in getValue, expecting a string for " + \
            "the second parameter, got " + str(paramName)
   if paramName == '':
      raise ValueError, "in getValue, the second parameter " + \
            "cannot be an empty string"
   if paramName[-1] != ':':
      raise ValueError, "in getValue, expecting the second parameter " + \
            "to end with a ':', got " + str(paramName)
   try:
      _getVal(anHTTPmsg, paramName)
   except ValueError:
      return False
   else:
      return True

