from StockPortfolio import *

exch = StockPortfolio("stock_data.txt")

exch.BuyStock("DAY.DB.C-T", 12)
print("Total Expenditures... " + str(exch.Expenditures()))
print("Total value of holdings... " + str(exch.ValueOfHoldings()) + "\n")

exch.BuyStock("ABX-T", 7)
print("Total Expenditures... " + str(exch.Expenditures()))
print("Total value of holdings... " + str(exch.ValueOfHoldings()) + "\n")

exch.SellStock("DAY.DB.C-T", 5)
print("Total Expenditures... " + str(exch.Expenditures()))
print("Total value of holdings... " + str(exch.ValueOfHoldings()) + "\n")

print("Profit is... " + str(exch.Profit()))

#Sell stock you don't own
#exch.SellStock("RIM-T", 12)
# print("Total Expenditures... " + str(exch.Expenditures()))
# print("Total value of holdings... " + str(exch.ValueOfHoldings()))