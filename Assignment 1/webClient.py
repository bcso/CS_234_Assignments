"""CS 234 Assignment 1 Question 2 - a simple web client
"""
import socket  
 
HTTP_PORT = 80
BUFFER_SIZE = 262144

websiteName  = 'www.google.ca'

def sendMessage(aWebsiteName, aMessage):
    """
    Preconditions: provide a valid string website name, and a string message
    Postcondition: send the message to the specified website and print a reply
    """

    if (type(aWebsiteName) != type("s")):
        raise TypeError, "website name must be a string"
    elif (type(aMessage) != type("s")):
          raise TypeError, "message must be a string"
    else:        
          getPageMsg = "GET http://" + aWebsiteName + "/HTTP/1.1\r\n\r\n"
          bSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          print aWebsiteName
          websiteIPAddr = socket.gethostbyname(aWebsiteName)
          bSocket.connect((websiteIPAddr, HTTP_PORT))
          print ("Connected to " + websiteIPAddr)
          bSocket.sendall(getPageMsg)
          print ("Received the following reply...")
          print (bSocket.recv(BUFFER_SIZE))
          bSocket.close()
          

website = raw_input("Enter your website...: ")
message = raw_input("Enter your message...: ")
sendMessage(website, message)

#Format of the HTTP message to ask for a web page
getPageMsg = "GET http://www.google.ca/ HTTP/1.1\r\n\r\n"

# create a communication channel through the internet (using TCP)
aSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# convert website name into an IP address, like 74.125.226.120
print websiteName
websiteIPAddr = socket.gethostbyname(websiteName)

#Connect to remote website
aSocket.connect( (websiteIPAddr, HTTP_PORT) )
print ("Connected to " + websiteIPAddr )
 
# Send message 
aSocket.sendall(getPageMsg)
print("Sent message: " + getPageMsg)
 
# Receive response
print("Received the following reply...")
print(aSocket.recv(BUFFER_SIZE))

# close the connection
aSocket.close()
 
