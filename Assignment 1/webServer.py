"""CS 234 Assignment 1 Question 1 - a simple web server
"""
import socket               

HTTP_PORT = 8080  
BUFFER_SIZE = 4096  
LOOPBACK_ADDR = '127.0.0.1'
MAX_NUM_CONNECTIONS = 1

def messageInHTML(aMessageTitle, aMessage):
   """
   Precondition: A string message and title
   Postcondition: A formatted string in HTML format containing the message and title 
   """
   
   return """<html>
   <head>
   <meta http-equiv="content-type" content="text/html; charset=UTF-8">
   <title>WebFilter</title>
   </head>
   <body>
   <h1>
      %s
   </h1>
   <p>
      %s
   </p>
   </body>
   </html>""" % (aMessageTitle, aMessage) 

def runWebFilter(HTTP_port):
   """
   Precondition: a valid integer port
   Postcondition: Return a message in the web browser at the socket and specified port
   """

   if (type(HTTP_port) != type(1)):
      raise TypeError, "Specified port must be an integer."
   else:
      # Create a communication channel (using TCP)
      bSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      # Associate the socket with a port
      bSocket.bind( (LOOPBACK_ADDR, HTTP_port) )        
      print ("socket bound to %s" %(HTTP_port))

      # Wait for connections
      bSocket.listen(MAX_NUM_CONNECTIONS)     

      # Accept 1 message
      for i in range(1):
         # Accept a socket connection with a client
         connection, addr = aSocket.accept()     
         print('Got connection from ' + str(addr))         
         msg = connection.recv(BUFFER_SIZE))
         message = messageInHTML('This is what the browser sent...', msg)         
         connection.sendall(message)
   
myResponse = """<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<title>WebFilter</title>
</head>

<body>
   HTMLMessage
<br>
 Message
</body>
</html>
"""

#Prompt user for input for a custom message
title = raw_input("Enter a title! : ")
message = raw_input("Enter a message! : ")
HTMLMessage = messageInHTML(title, message)

# Create a communication channel (using TCP)
aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associate the socket with a port
aSocket.bind( (LOOPBACK_ADDR, HTTP_PORT) )        
print ("socket bound to %s" %(HTTP_PORT))

# Wait for connections
aSocket.listen(MAX_NUM_CONNECTIONS)     

# Accept 1 message
for i in range(1):
   # Accept a socket connection with a client
   connection, addr = aSocket.accept()     
   print('Got connection from ' + str(addr))
   print('The message is:')
   print(connection.recv(BUFFER_SIZE))
   print(HTMLMessage)
   connection.sendall(HTMLMessage)

connection.close() 
print "Closed server"
