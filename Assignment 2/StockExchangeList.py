# import the contents of the Stock class, 
# making all function names local to this class
from Stock import *

class StockExchange:
   """
    A list-based implementation of ADT Stock Exchange.
    ADT StockExchange is a container where the elements 
    represent stocks on a stock exchange.
    Field: _stocks - a list of all the Stocks
   """
   
   def __init__(self, fname):
      """
      Precondition: fname is a filename containing data taken from
        the TSX stock listing of http://www.globeinvestor.com/
      Postcondition: return a StockExchange data type
      """
      try:
         # underscore (i.e. _stocks) means it should not be used 
         # by methods outside this class
         self._stocks = []
         F = open(fname)
         L = F.readlines()
         # build a stock from each line beyond the 2 header rows
         for line in L[2:]:
            # strip each piece from last "Stock" to end 
            # line.split() creates a list of words from 'line'
            # line is a string, data is a list of strings
            data = line.split()
            # data.pop(-1) removes the last item from a list
            while data[-1] != "Stock":
               data.pop(-1)

            # grab data: work from the end of the line to the beginning
            # because we are not sure how many spaces in stock name
            
            # Note: volume has commas in the data file - remove them
            # can convert string like "12.50" to float but not directly to int
            volume = float(data[-4].replace(",",""))
            # now convert float 12.50 to int 12
            volume = int(volume)
            low = float(data[-5])
            high = float(data[-6])
            price = float(data[-10])
            symbol = data[-11]

            # build name by concatenating pieces before symbol
            name = ""
            for x in data[0:-11]:
               name = name + x
            stock = Stock(name,symbol,price,low,high,volume)
            self._stocks.append(stock)
      # capture any exception, store its description in variable e
      except Exception as e:
         print (e)



   def __contains__(self, aSymbol):
      """
      Precondition: aSymbol is a string
      Postcondition: returns True iff there is a stock with
        aSymbol listed in the StockExchange
      """
      return Stock("name ignored",aSymbol) in self._stocks

   
   def add(self, aStock):
      """
      Precondition: aStock is of type Stock
      Postcondition: adds aStock to the stock exchange
      """
      self._stocks.append(aStock)
   

   def remove(self, aSymbol):
      """
      Precondition: aSymbol is a valid stock symbol
      Postcondition: remove the Stock with aSymbol from the StockExchange
      """
      self._stocks.remove(Stock("name ignored",aSymbol))
   
      """
      Precondition: aSymbol represents a Stock in the StockExchange
      Postcondition: returns the price of this stock as a float
      """


   def getPrice(self, aSymbol):
      """
      Precondition: aSymbol represents a Stock in the StockExchange
      Postcondition: returns the price of this stock as a float
      """
      stock = self._findStock(aSymbol)
      return stock.price
   

   def sell(self, aSymbol, aPrice):
      """
      Precondition: aSymbol represents a Stock in the StockExchange
      Postcondition: changes the price of stock to aPrice
         the high or low value will be changed if appropriate
         the volume of stock will increase by 1
      """
      stock = self._findStock(aSymbol)
      stock.price = aPrice
      if stock.price < stock.low:
         stock.low = stock.price
      if stock.price > stock.high:
         stock.high = stock.price
      stock.volume = stock.volume + 1


   # leading underscore _xyz means xyz is meant to be a private function
   def _findStock(self, aSymbol):
      """
      Preconditions: aSymbol is a valid stock symbol
      Postconditions: return the Stock corresponding to aSymbol
      """
      for stock in self._stocks:
         if stock.symbol == aSymbol:
            return stock

         
   def biggestGainers(self):
      """
      Postcondition: returns a list of up to 10 stocks with
         the biggest jump from its low to current price.
         Assumes s.low <= s.price for all stocks in the exchange
         The answer is sorted from largest to smallest jump.
         To break ties, the alphabetical order of the symbols is used. That is,
         if stocks are tied for 10th place, the one appearing earlier in 
         alphabetical order by symbol is considered in the top 10.
         If there are fewer than 10 stocks, then produces list of all stocks
      """
      # first sort alphabetically by symbol
      self._stocks.sort(key = lambda stock: stock.symbol)
      # now sort by gain
      # those with same gain will still be sorted by symbol
      self._stocks.sort(key = lambda stock: stock.low - stock.price)
      return self._stocks[0:10]

  
