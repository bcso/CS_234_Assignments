from StockPortfolio import *

def approxEquals(x1, x2, epsilon = 0.005):
   """return True if x1 is within epsilon of x2"""
   return (x1 > (x2 - epsilon)) and (x1 < (x2 + epsilon))

def main():
   print "Testing StockPortfolio on bad input"

   #
   # constructor
   #
   try:
      sp1 = StockPortfolio(1.0)
   except TypeError:
      print ("Passed Test 1, improper constructor")
   except Exception:
      print ("Failed Test 1, improper constructor")
  
   #
   # CurrentPrices
   #
   sp1 = StockPortfolio("test_data1.txt")
   try:
      sp1.CurrentPrices(1.0)
   except TypeError:
      print ("Passed Test 2, CurrentPrices: improper type")
   except Exception:
      print ("Failed Test 2, CurrentPrices: improper type")
  
   #
   # BuyStock
   #
   try:
      sp1.BuyStock(100, 100)
   except TypeError:
      print ("Passed Test 3, BuyStock: improper stock name type")
   except Exception:
      print ("Failed Test 3, BuyStock: improper stock name type")
  
   try:
      sp1.BuyStock("AAPL", "AAPL")
   except TypeError:
      print ("Passed Test 4, BuyStock: improper number of shares type")
   except Exception:
      print ("Failed Test 4, BuyStock: improper number of shares type")
   
   try:
      sp1.BuyStock("XYZ", 100)
   except ValueError:
      print ("Passed Test 5, BuyStock: no such stock name")
   except Exception:
      print ("Failed Test 5, BuyStock: no such stock name")

   try:
      sp1.BuyStock("AAPL", -1)
   except TypeError:
      print ("Passed Test 6, BuyStock: number of shares must be positive")
   except Exception:
      print ("Failed Test 6, BuyStock: number of shares must be positive")

   #
   # SellStock
   #
   sp1.BuyStock("AAPL", 100)
   try:
      sp1.SellStock(100, 100)
   except TypeError:
      print ("Passed Test 7, SellStock: improper stock name type")
   except Exception:
      print ("Failed Test 7, SellStock: improper stock name type")
  
   try:
      sp1.SellStock("AAPL", "AAPL")
   except TypeError:
      print ("Passed Test 8, SellStock: improper number of shares type")
   except Exception:
      print ("Failed Test 8, SellStock: improper number of shares type")
   
   try:
      sp1.SellStock("XYZ", 100)
   except ValueError:
      print ("Passed Test 9, SellStock: no such stock name")
   except Exception:
      print ("Failed Test 9, SellStock: no such stock name")

   #sp1.SellStock("AAPL", -1)
   try:
      sp1.SellStock("AAPL", -1)
   except ValueError:
      print ("Passed Test 10, SellStock: number of shares must be positive")
   except Exception:
      print ("Failed Test 10, SellStock: number of shares must be positive")

   try:
      sp1.SellStock("AAPL", 101)
   except ValueError:
      print ("Passed Test 11, SellStock: more shares than you own")
   except Exception:
      print ("Failed Test 11, SellStock: more shares than you own")


   print ("\nTesting StockPortfolio on good input")

   sp2 = StockPortfolio("test_data1.txt")
   if approxEquals(sp2.ValueOfHoldings(), 0.0):
      print ("Passed Test 12, ValueOfHoldings")
   if approxEquals(sp2.Expenditures(), 0.0):
      print ("Passed Test 13, Expenditures")
   if approxEquals(sp2.Profit(), 0.0):
      print ("Passed Test 14, Profit")

   sp2.BuyStock("AAPL", 10)
   if approxEquals(sp2.ValueOfHoldings(), 6000.0):
      print ("Passed Test 15, ValueOfHoldings")
   if approxEquals(sp2.Expenditures(), 6000.0):
      print ("Passed Test 16, Expenditures")
   if approxEquals(sp2.Profit(), 0.0):
      print ("Passed Test 17, Profit")
             
   sp2.CurrentPrices("test_data2.txt")
   sp2.SellStock("AAPL", 10)
   if approxEquals(sp2.ValueOfHoldings(), 0.0):
      print ("Passed Test 18, ValueOfHoldings")
   if approxEquals(sp2.Expenditures(), -500.0):
      print ("Passed Test 19, Expenditures")
   if approxEquals(sp2.Profit(), 500.0):
      print ("Passed Test 20, Profit")

   sp2 = StockPortfolio("test_data1.txt")
   sp2.BuyStock("GOOG", 10)
   if approxEquals(sp2.ValueOfHoldings(), 6000.0):
      print ("Passed Test 21, ValueOfHoldings")
   if approxEquals(sp2.Expenditures(), 6000.0):
      print ("Passed Test 22, Expenditures")
   if approxEquals(sp2.Profit(), 0.0):
      print ("Passed Test 23, Profit")

   sp2.CurrentPrices("test_data2.txt")
   sp2.SellStock("GOOG", 10)
   if approxEquals(sp2.ValueOfHoldings(), 0.0):
      print ("Passed Test 24, ValueOfHoldings")
   if approxEquals(sp2.Expenditures(), 500.0):
      print ("Passed Test 25, Expenditures")
   if approxEquals(sp2.Profit(), -500.0):
      print ("Passed Test 26, Profit")

main()
