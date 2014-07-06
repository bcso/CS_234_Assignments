"""
Implements a 2x2 matrix with integer entries
"""

import math

class IntMatrix(object) :

   #
   # Constructors
   #
   
   def __init__(self, e11, e12, e21, e22):
      self.x11 = e11
      self.x12 = e12
      self.x21 = e21
      self.x22 = e22
 
   #
   # Boolean Operators
   #
   
   def __eq__(self, rhs):
     return ( (self.x11 == rhs.x11) and (self.x12 == rhs.x12) and \
              (self.x21 == rhs.x21) and (self.x22 == rhs.x22) )

   def __ne__(self, rhs):
      return not (self == rhs)

   #
   # Conversion Functions
   #

   def __str__(self):
      return "%4d %4d\n%4d %4d" %(self.x11, self.x12, self.x21, self.x22)
 
   #
   # Arithmetic Operators
   #

   def __add__(self, rhs):
      return IntMatrix(self.x11+rhs.x11, self.x12+rhs.x12, \
                       self.x21+rhs.x21, self.x22+rhs.x22)

   def __sub__(self, rhs):
      return IntMatrix(self.x11-rhs.x11, self.x12-rhs.x12, \
                       self.x21-rhs.x21, self.x22-rhs.x22)

   def __mul__(self, rhs):
      return IntMatrix(self.x11*rhs.x11 + self.x12+rhs.x21, \
                       self.x11*rhs.x21 + self.x12+rhs.x22, \
                       self.x21*rhs.x11 + self.x22+rhs.x21, \
                       self.x21*rhs.x21 + self.x22+rhs.x22)
   #
   # Matrix Operators
   #

   def det(self):
      return ((self.x11 * self.x22) - (self.x12 * self.x21))




