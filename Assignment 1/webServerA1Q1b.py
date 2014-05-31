"""CS 234 Assignment 1 Question 1 - a simple web server
"""
import socket               

BUFFER_SIZE = 4096  
LOOPBACK_ADDR = '127.0.0.1'
MAX_NUM_CONNECTIONS = 1


def messageInHTML(aMessageTitle, aMessage):
   """ format aMesssageTitle and aMessage in html format
   """
   return """<html>
   <head>
   <meta http-equiv="content-type" content="text/html; charset=UTF-8">
   <title>WebFilter</title>
   </head>
   <body> <h2>%s</h2> <br>%s </body>
   </html>
   """ %(aMessageTitle, aMessage)

def runWebFilter(aPort):
   """ create a web server that echo back what it receives in html format
   """
   # Create a communication channel (using TCP)
   aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # Associate the socket with a port
   aSocket.bind( (LOOPBACK_ADDR, aPort) )        
   print ("socket bound to %s" %(aPort))

   # Wait for connections
   aSocket.listen(MAX_NUM_CONNECTIONS)     

   # Accept 1 message
   for i in range(1):
      # Accept a socket connection with a client
      connection, addr = aSocket.accept()     
      print('Got connection from ' + str(addr))
      
      # Save the message received in msg
      msg =connection.recv(BUFFER_SIZE)

      # Send back the message in HTML format
      connection.sendall(messageInHTML("This is what the browser sent...", msg))

   connection.close() 
   print "Server closed"
