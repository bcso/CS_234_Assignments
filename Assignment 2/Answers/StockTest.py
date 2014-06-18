from StockA2 import Stock

def testStock():
   """Precondition: import a class called Stock
      Postcondition Test the Constructor function for the class Stock
      for TypeErrors and ValueErrors"
   """

   # aName
   try:
      Stock(1, "RIM", 2.00, 1.00, 3.00, 10000)
   except TypeError:
      print ("Passed Test 1, Company Name")
   except Exception:
      print ("Failed Test 1, Company Name")
   try:
      Stock("", "RIM", 2.00, 1.00, 3.00, 10000)
   except ValueError:
      print ("Passed Test 2, Company Name")
   except Exception:
      print ("Failed Test 2, Company Name")


   # aSymbol
   try:
      Stock("Blackberry", 1.2, 2.00, 1.00, 3.00, 10000)
   except TypeError:
      print ("Passed Test 3, Trading Symbol")
   except Exception:
      print ("Failed Test 3, Trading Symbol")
   try:
      Stock("Blackberry", "", 2.00, 1.00, 3.00, 10000)
   except ValueError:
      print ("Passed Test 4, Trading Symbol")
   except Exception:
      print ("Failed Test 4, Trading Symbol")

   # price
   try:
      Stock("Blackberry", "RIM", 1, 1.00, 3.00, 10000)
   except TypeError:
      print ("Passed Test 5, Price")
   except Exception:
      print ("Failed Test 5, Price")
   try:
      Stock("Blackberry", "RIM", -1.2, 1.00, 3.00, 10000)
   except ValueError:
      print ("Passed Test 6, Price")
   except Exception:
      print ("Failed Test 6, Price")

   # low
   try:
      Stock("Blackberry", "RIM", 2.00, 1, 3.00, 10000)
   except TypeError:
      print ("Passed Test 7, Low")
   except Exception:
      print ("Failed Test 7, Low")
   try:
      Stock("Blackberry", "RIM", 2.00, -1.2, 3.00, 10000)
   except ValueError:
      print ("Passed Test 8, Low")
   except Exception:
      print ("Failed Test 8, Low")
   try:
      Stock("Blackberry", "RIM", 2.00, 2.10, 3.00, 10000)
   except ValueError:
      print ("Passed Test 9, Low")
   except Exception:
      print ("Failed Test 9, Low")

   # high
   try:
      Stock("Blackberry", "RIM", 2.00, 1.00, 3, 10000)
   except TypeError:
      print ("Passed Test 10, High")
   except Exception:
      print ("Failed Test 10, High")
   try:
      Stock("Blackberry", "RIM", 2.00, 1.00, -1.2, 10000)
   except ValueError:
      print ("Passed Test 11, High")
   except Exception:
      print ("Failed Test 11, High")
   try:
      Stock("Blackberry", "RIM", 2.00, 1.00, 1.90, 10000)
   except ValueError:
      print ("Passed Test 12, High")
   except Exception:
      print ("Failed Test 12, High")

   # volume
   try:
      Stock("Blackberry", "RIM", 2.00, 1.00, 3.00, 10000.0)
   except TypeError:
      print ("Passed Test 13, Volume")
   except Exception:
      print ("Failed Test 13, Volume")
   try:
      Stock("Blackberry", "RIM", 2.00, -1.2, -1.2, -1000)
   except ValueError:
      print ("Passed Test 14, Volume")
   except Exception:
      print ("Failed Test 14, Volume")


testStock()
