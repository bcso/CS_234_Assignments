from types import StringType, FloatType, IntType

from StockExchangeList import *

class StockPortfolio (object) :
   """
   Track the holdings of stock and the ongoing profits and loses
   associated with them.
   """
   def __init__(self, aStockListingsFile):
      """
      Precondition: fname is a filename containing data taken from
      the TSX stock listing of http://www.globeinvestor.com/
      Postcondition: return a StockPortfolio data type
      """
      # test preconditions on aStockListingsFile by calling CurrentPrices
      self.CurrentPrices(aStockListingsFile)
      self._expenditures = 0.0
      self._holdings = {} # key is stock symbol, value is # of shares


   def CurrentPrices(self, aStockListingsFile):
      """
      Precondition: fname is a filename containing data taken from
      the TSX stock listing of http://www.globeinvestor.com/
      Postcondition: set self._listings to a StockExchange data type
      """
      
      # test preconditions
      if type(aStockListingsFile) != StringType:
         raise TypeError, "in StockPortfolio, expecting a string, got " + \
         str(aStockListingsFile)
    
      try:
         self._listings = StockExchange(aStockListingsFile)
      except Exception:
         raise IOError, "StockPortfolio: " + aStockListingsFile + \
             "is not a valid stock listings file" 
      self._listings = StockExchange(aStockListingsFile)


   def BuyStock(self, aSymbol, numShares):
      """ Preconditions:
           aSymbol is a string and a valid stock symbol
           numShares is a positive integer
      Postconditions: add numShares of the stock aSymbol to  _holdings
        and increase _expenditures by the cost of purchasing the stock
      """

      # test preconditions
      if type(aSymbol) != StringType:
         raise TypeError, "in BuyStock, for stock symbol, expecting " + \
                           "a string, got " + str(aName)
      if type(numShares) != IntType and type(numShares) != FloatType:
         raise TypeError, "in BuyStock, for number of shares, expecting " + \
          "a number, got " + str(aName)

      if aSymbol not in self._listings:
         raise ValueError, "BuyStock: there is no stock called " + aSymbol
      if type(numShares) < 1:
         raise ValueError, "BuyStock, the number of shares must be a" + \
               "postivie number, got " + str(numShares)

      # update holdings and expenditures
      if aSymbol in self._holdings:
         self._holdings[aSymbol] += numShares
      else:
         self._holdings[aSymbol] = numShares
      self._expenditures += numShares * self._listings.getPrice(aSymbol)
         
   

   def SellStock(self, aSymbol, numShares):
      """ Preconditions:
           aSymbol is a string and a valid stock symbol in _holdings
           numShares is a positive integer, <= the number of shares in _holdings
      Postconditions: sell numShares of the stock aSymbol
          and decrease _expenditures by the revenue of selling the stock
      """
      # test preconditions
      if type(aSymbol) != StringType:
         raise TypeError, "in SellStock, for stock symbol, expecting " + \
                           "a string, got " + str(aName)
      if type(numShares) != IntType and type(numShares) != FloatType:
         raise TypeError, "in SellStock, for number of share, expecting a " + \
          "number, got " + str(aName)

      if aSymbol not in self._holdings:
         raise ValueError, "in SellStock: you do not own the stock " + aSymbol
      if numShares < 1:
         raise ValueError, "SellStock, the number of shares must be a" + \
               "postivie number, got " + str(numShares)
      if numShares > self._holdings[aSymbol]:
         raise ValueError, ("SellStock: you do not own %d shares of " % \
                            numShares) + aSymbol

      # update holdings and expenditures
      self._expenditures -= numShares * self._listings.getPrice(aSymbol)
      self._holdings[aSymbol] -= numShares

      
   def Expenditures(self):
      """  Postcondition: return the total amount of expenditures
      """
      return self._expenditures


   def ValueOfHoldings(self):
      """  Postcondition: return the total value of all the holdings
      """
      answer =0.0
      for aSym in self._holdings:
        if aSym in self._listings:
           answer += self._listings.getPrice(aSym) * self._holdings[aSym]
      return answer
   

   def Profit(self):
      """  Postconditions: return the total value of holdings minus
           the expenditures.
      """
      return self.ValueOfHoldings() - self.Expenditures()

