from Stock import Stock

def testStock():
	try:		
		stock = Stock(2, "ns", 4.0, 1.0, 9.0, 10.0)
	except TypeError, e:
		print e
		pass

	try:		
		stock = Stock("", "ns", 4.0, 1.0, 9.0, 10.0)		
	except TypeError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", 2, 4.0, 1.0, 9.0, 10.0)
	except TypeError, e:
		print e
		pass
	
	try:		
		stock = Stock("NewStock", "", 4.0, 1.0, 9.0, 10.0)
	except TypeError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", -4.0, 1.0, 9.0, 10.0)
	except ValueError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", 4.0, -1.0, 9.0, 10.0)
	except ValueError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", 4.0, 1.0, -9.0, 10.0)
	except ValueError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", 4.0, 1.0, 9.0, -10.0)
	except ValueError, e:
		print e
		pass			

	try:		
		stock = Stock("NewStock", "bl", 4.0, 7.0, 9.0, 10.0)
	except ValueError, e:
		print e
		pass	

	try:		
		stock = Stock("NewStock", "bl", 10.0, 1.0, 9.0, 10.0)
	except ValueError, e:
		print e
		pass	

	try:		
		stock = Stock("NewStock", "bl", 4.0, 10.0, 9.0, 10.0)
	except ValueError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", 4, 1.0, 9.0, 10.0)
	except ValueError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", 4.0, 1, 9.0, 10.0)
	except ValueError, e:
		print e
		pass

	try:		
		stock = Stock("NewStock", "bl", 4.0, 1.0, 9, 10.0)
	except ValueError, e:
		print e
		pass


testStock()