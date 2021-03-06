import socket  
 
HTTP_PORT = 80
BUFFER_SIZE = 262144
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
   <body> <h2>%s</h2><br>%s</body>
   </html>
   """ %(aMessageTitle, aMessage)



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

   # close the connection
   aSocket.close()
 


def getHost(anHTTPmsg):
   """ get the name of the host for anHTTPmsg
   """
   try:
      for line in anHTTPmsg.splitlines():
         words = line.split()
         if (words[0] == "Host:") and (len(words)>1):
             return words[1]
      raise ValueError, "cannot find 'Host:' keyword in HTTP message"
   except Exception:
      raise ValueError, "cannot find host in HTTP message"
   


def runWebFilter(aPort):
   """ create a web server that echo back what it receives in html format
   """
   # Create a communication channel (using TCP)
   aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # Associate the socket with a port
   aSocket.bind( (LOOPBACK_ADDR, aPort) )        

   # Wait for connections
   aSocket.listen(MAX_NUM_CONNECTIONS)     

   # Accept 1 message
   for i in range(1):
      # Accept a socket connection with a client
      connection, addr = aSocket.accept()     
      
      # Save the message received in msg
      msg =connection.recv(BUFFER_SIZE)

      try:
         host = getHost(msg)
      except ValueError:
         connection.sendall(messageInHTML("Error: Host not found", msg))
      else:  
         sendMessage(host, msg)
         connection.sendall(messageInHTML("This is what the browser sent...", msg))

   connection.close() 
 

