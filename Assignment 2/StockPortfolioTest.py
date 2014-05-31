from StockPortfolio import *
from StockExchangeList import *

portfolio = StockPortfolio("stock_data.txt")
exch = StockExchange("stock_data.txt")

portfolio.BuyStock("DAY.DB.C-T", 12)
assert portfolio.Expenditures() == (exch.getPrice("DAY.DB.C-T") * 12)
assert portfolio.ValueOfHoldings() == (exch.getPrice("DAY.DB.C-T") * 12)

portfolio.BuyStock("ABX-T", 7)
assert portfolio.Expenditures() == (exch.getPrice("DAY.DB.C-T") * 12 + exch.getPrice("ABX-T") * 7)
assert portfolio.ValueOfHoldings() == (exch.getPrice("DAY.DB.C-T") * 12 + exch.getPrice("ABX-T") * 7)

portfolio.SellStock("DAY.DB.C-T", 5)
assert portfolio.Expenditures() == (exch.getPrice("DAY.DB.C-T") * 12 + exch.getPrice("ABX-T") * 7 - exch.getPrice("DAY.DB.C-T") * 5)
assert portfolio.ValueOfHoldings() == (exch.getPrice("DAY.DB.C-T") * (12-5) + exch.getPrice("ABX-T") * 7)

# Value of all stocks is equal to the amount you have paid for them, there is not change in stock value
assert str(portfolio.Profit() == 0)

print("Total Expenditures... " + str(portfolio.Expenditures()))
print("Total ValueOfHoldings... " + str(portfolio.ValueOfHoldings()))
print("Profit is... " + str(portfolio.Profit()))
