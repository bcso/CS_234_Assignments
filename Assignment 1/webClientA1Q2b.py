import socket  
 
HTTP_PORT = 80
BUFFER_SIZE = 262144


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
 
