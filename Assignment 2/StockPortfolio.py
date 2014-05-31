from StockExchangeList import *
from Stock import *
import os

class StockPortfolio:

	def __init__(self, aStockListingsFile):
		"""
		Pre-conditions: aStockListingsFile is a string reference to a text file which exists
		"""
		try:	
			if type(aStockListingsFile) != type("s"):
				raise TypeError, "Input file name must be a string"
			else: 
				F = open(aStockListingsFile)
				L = F.readlines()
				self._newStockSymbols = []

				#Grab all the stock symbols in aStockListingsFile as a list for reference
				for line in L[2:]:
					data = line.split()
					while data[-1] != "Stock":
						data.pop(-1)					
					symbol = data[-11]
					self._newStockSymbols.append(symbol)

				self._exch = StockExchange(aStockListingsFile)
				self.totalExpenditures = 0.0
				self._valueOfHoldings = {}
		except IOError, e:
			print e

	def CurrentPrices(self, aStockListingsFile):
		"""
		Pre-conditions: aStockListingsFile is a string reference to a text file which exists
		Post-conditions: The specified aStockListingsFile will be used as the new updated stock sheet
		"""
		try:
			if type(aStockListingsFile) != type("s"):
				raise TypeError, "Input file name must be a string"
			else:
				self._exch = StockExchange(aStockListingsFile)
		except IOError, e:
			print e

	def BuyStock(self, aSymbol, numShares):
		"""	
		Pre-conditions: numShares must be an integer, aSymbol must exist in the data
		Post-conditions: expenditures and value of holdings will increase in value equal to the amount of money spent buying the stock
		"""
		if (aSymbol in self._newStockSymbols) == False:
			raise ValueError, "Stock symbol must exist."
		elif type(numShares) != type(1):
			raise TypeError, "Number of Shares must be an integer"
		else:

			price = self._exch.getPrice(aSymbol)
			print("Price per share: " + str(price))
			totalPrice = numShares * price
			self.totalExpenditures += totalPrice
			if (aSymbol in self._valueOfHoldings) == False:
				#Create new stock key
				self._valueOfHoldings[aSymbol] = numShares
			elif (aSymbol in self._valueOfHoldings) == True:
				# Simply update the value already associated with the stock
				self._valueOfHoldings[aSymbol] += numShares


	def SellStock(self, aSymbol, numShares):
		"""	
		Pre-conditions: numShares must be an integer, aSymbol must exist in the data,
						must own the stock, cannot sell more than you own
		Post-conditions: expenditures and value of holdings will decrease in value equal to the amount of money spent buying the stock
		"""	
		if type(numShares) != type(1):
			raise TypeError, "Number of Shares must be an integer"
		else:		
			if (aSymbol in self._newStockSymbols) == False:
				#Set stock value to 0 if it doesn't exist in the data file
				stockValue = 0
			else:
				#Calculate total price for number of shares to buy
				price = self._exch.getPrice(aSymbol)
				print("Price per share: " + str(price))
				totalPrice = numShares * price
				self.totalExpenditures -= totalPrice


			if (aSymbol in self._valueOfHoldings) == False:
				# Check for existence of stock in your holdings
				raise ValueError, "Cannot sell stock you don't own!"			
			elif (aSymbol in self._valueOfHoldings) == True:
				if (numShares > self._valueOfHoldings[aSymbol]):
					# Check for case when you try to sell more than you own
					raise ValueError, "cannot sell more than you own!"
				else:
					# Simply update the value already associated with the stock
					self._valueOfHoldings[aSymbol] -= numShares

	def Expenditures(self):
		return self.totalExpenditures

	def ValueOfHoldings(self):
		# For all the values(#stock) in each key (stock symbol owned), calculate the total value and sum across all keys
		# by using the current stock price

		self.totalCurrentValue = 0.0
		for key in self._valueOfHoldings:
			currentValue = self._exch.getPrice(key) * float(self._valueOfHoldings[key])
			self.totalCurrentValue += currentValue

		return self.totalCurrentValue		

	def Profit(self):
		return self.totalCurrentValue - self.totalExpenditures 
		pass

