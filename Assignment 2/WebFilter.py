"""CS 234 Assignment 2 Question 3 - Course Project
"""

import socket
 
HTTP_PORT = 80
BUFFER_SIZE = 262144  
LOOPBACK_ADDR = '127.0.0.1'
MAX_NUM_CONNECTIONS = 1
HOST = ""
HOST_EXISTS = True

def sendMessage (aWebsiteName, aMessage):
   """ send aMessage to aWebsiteName and print response
   """

   # create a communication channel through the internet (using TCP)
   aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # convert website name into an IP address, like 74.125.226.120
   websiteIPAddr = socket.gethostbyname(aWebsiteName)

   #Connect to remote website
   aSocket.connect( (websiteIPAddr, HTTP_PORT) )
 
   # Send message 
   aSocket.sendall(aMessage)
 
   # Receive response
   print(aSocket.recv(BUFFER_SIZE))

def messageInHTML(aMessageTitle, aMessage):
   """
   Precondition: A string message and title
   Postcondition: A formatted string in HTML format containing the message and title 
   """
   if (type(aMessage) != "s") or (type(aMessageTitle) != "s"):
      raise TypeError, "message and message title must be string types"
   else: 
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

def runWebFilter(aPort):
   """
   Precondition : a valid port integer
   Postcondition : Send a message recieved from the website specified to the browser
   """
   try:
      if type(aPort) != type(1):
         raise TypeError, "Port number must be an integer"
      else:
         # Create a communication channel (using TCP)
         aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

         # Associate the socket with a port
         aSocket.bind( (LOOPBACK_ADDR, aPort) )           

         # Wait for connections
         aSocket.listen(MAX_NUM_CONNECTIONS)

         # Accept a socket connection with a client
         connection, addr = aSocket.accept()        

         # Save the message received in msg
         msg = connection.recv(BUFFER_SIZE)
         
         #Get the host from the message recieved
         host = getHost(msg)
                        
         # Print the message out on the screen  
         sendMessage(host, msg)

         #Send the message back to the browser
         connection.sendall(messageInHTML("This is what the browser sent...", msg))

         aSocket.close()   

   except Exception, e:
      connection.sendall(messageInHTML("This is what the browser sent...", "Error: Host not found"))

def getHost(anHTTPcmd):
   """
   Precondition : anHTTPcmd must be a string type
   Postcondition : fetch the host name from anHTTPcmd
   """
   if type(anHTTPcmd) != type("s"):
      raise TypeError, "anHTTPcmd must be a string type"
   else: 
      try:
         lines = anHTTPcmd.splitlines()
         for line in lines:
            words = line.split()
            for word in words:
               if word == "Host:":
                  HOST = words.pop(-1)
                  socket.gethostbyname(HOST)               
                  return HOST
                  break
      except socket.error:
         raise Exception
