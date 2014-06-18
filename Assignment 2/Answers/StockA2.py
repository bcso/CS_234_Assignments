from types import StringType, FloatType, IntType

class Stock:
   """
   A data type collecting the attributes of a single stock
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
      # aName
      if type(aName) != StringType:
         raise TypeError, "in Stock, for company name, expecting a string, got " + \
         str(aName)
      if aName == "":
         raise ValueError, "in Stock, the company name cannot be blank"
      self.name = aName

      # aSymbol
      if type(aSymbol) != StringType:
         raise TypeError, "in Stock, for trading symbol, expecting a string, got " + \
         str(aSymbol)
      if aSymbol == "":
         raise ValueError, "in Stock, the trading symbol cannot be blank"
      self.symbol = aSymbol

      # price
      if type(price) != FloatType:
         raise TypeError, "in Stock, for price, expecting a float, got " + \
         str(price)
      if price < 0.0:
         raise ValueError, "in Stock, the price cannot be negative, got " + \
         str(price)
      self.price = price

      # low
      if type(low) != FloatType:
         raise TypeError, "in Stock, for low, expecting a float, got " + \
         str(low)
      if low < 0.0:
         raise ValueError, "in Stock, the low cannot be negative, got " + \
         str(low)
      if low > price:
         raise ValueError, "in Stock, the daily low, %.2f,  cannot " % low  +\
         "be higher than the current price, %.2f" % price
      self.low = low

      # high
      if type(high) != FloatType:
         raise TypeError, "in Stock, for high, expecting a float, got " + \
         str(high)
      if high < 0.0:
         raise ValueError, "in Stock, the high cannot be negative, got " + \
         str(high)
      if high < price:
         raise ValueError, "in Stock, the daily high, %.2f,  cannot " % high  +\
         "be lower than the current price, %.2f" % price
      self.high = high

      # volume
      if type(volume) != IntType:
         raise TypeError, "in Stock, for volume, expecting an int, got " + \
         str(volume)
      if volume < 0:
         raise ValueError, "in Stock, the volume cannot be negative, got " + \
         str(volume)
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


