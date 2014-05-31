from StockExchangeList import *
from Stock import *

newExch = StockExchange("stock_data.txt")
print("example price... " + str(newExch.getPrice("ECA-T")))