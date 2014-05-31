"""CS 234 Assignment 2 Question 1a - Testing assumptions: Stock.py
"""
class Stock:
   """
   A data type representing a single stock
   Fields: name - str: the company name as a string 
           symbol - str: a string uniquely identifying the stock 
           price - non-negative float: last/current price 
           low - non-negative float: lowest price of the day
           high - non-negative float: highest price of the day 
           volume - non-negative int: number of shares traded 
   Floats are represented to two decimal places.
   The constraint low <= price <= high is always satisfied. 
   """

   def __init__(self, aName, aSymbol, price = 0.0,\
                low = 0.0, high = 0.0, volume = 0):
      """
      Preconditions: aName and aSymbol are strs 
      Assumptions: if supplied price, low and high are non-negative floats
                   if supplied volume is a non-negative int
                   low <= price <= high
      Postconditions: construct a stock data type with aName and aSymbol
      """

      if type(aSymbol) != type("s"):
        raise TypeError, "The input symbol must be a string!"
      if len(aSymbol) == 0:
        raise TypeError, "The input symbol cannot be empty!"        
      elif type(aName) != type("s"):
        raise TypeError, "The input name must be a string!"
      if len(aName) == 0:
        raise TypeError, "The input name cannot be empty!"          
      elif (price < 0) or (low < 0) or (high < 0) or (volume < 0):
        raise ValueError, "Price, low, high and volume inputs must be non-negative!"
      elif (low <= price) == False:
        raise ValueError, "Low must be lower than price!"
      elif (price <= high) == False:
        raise ValueError, "Price must be lower than high!"
      elif (low <= high) == False:
        raise ValueError, "Low must be lower than high!"
      elif (type(price) != type(0.0)) or (type(low) != type(0.0)) or (type(high) != type(0.0)):
        raise ValueError, "Price, low and high inputs must be float inputs!"
             
      self.name = aName
      self.symbol = aSymbol
      self.price = price
      self.low = low
      self.high = high
      self.volume = volume 


   def __repr__(self):
      """
      Postcondition: return a string representation of Stock
      """
      return "Stock(%s, %s, %.2f, %.2f, %.2f, %d)" % \
             (self.name, self.symbol, self.price, \
              self.low, self.high, self.volume)
     

   def __eq__(self, rhs):
      """
      Precondition: rhs is another Stock
      Postcondition: returns True iff both stock symbols are identical
      """
      return self.symbol == rhs.symbol
        

   def __ne__(self, rhs):
      """
      Precondition: rhs is another Stock
      Postcondition: returns True iff both stock symbols are different
      """
      return not(self==rhs)


