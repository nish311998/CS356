'''
Nishanth Gona
ng334
CS356-006
'''

import sys, os
import datetime, time          #given to us in programming assignment document
from socket import *



def cache():
    exists = os.path.isfile('cache.txt') #check for file https://therenegadecoder.com/code/how-to-check-if-a-file-exists-in-python/
    if exists:
        f=open('cache.txt', 'r')
        contents = f.read()
        f.close()
        if  contents == '':
            return 'empty'
        else:
            return contents.find(filename) #just telling us either the location of the filename or if not there then return -1
            
    else:
        
        return 'empty'

# Get the server hostname, port and data length as command line arguments
argv = sys.argv
url = argv[1]
host, data = url.split(':')
port, filename = data.split('/')

#Check if file is in cache

val = cache()
if val == 'empty' or val == -1:
    # get
    data = "GET   /"+filename+"   HTTP/1.1\r\nHost:  "+host+":"+port+"\r\n\r\n"

else:
    #use conditonal get
    f=open('cache.txt', 'r')
    contents = f.read()
    f.close()
    index = contents.find('L')
    mod = contents[index+15:index+44]
    data = "GET   /"+filename+"   HTTP/1.1\r\nHost:  "+host+":"+port+"\r\nIf-Modified-Since: "+mod+"\r\n\r\n"  
                         
 
# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket = socket(AF_INET, SOCK_STREAM)
# Create TCP connection to server
clientSocket.connect((host, int(port)))
# Send data through TCP connection
print("HTTP Request:\r\n"+data)
clientSocket.send(data.encode())
# Receive the server response
dataEcho = clientSocket.recv(10000)

# Display the server response as an output
print("HTTP Response:\r\n"+dataEcho.decode())

if dataEcho.decode().find('200') != -1:
    Lval = dataEcho.decode().find('L')
    mod = dataEcho.decode()[Lval+15:Lval+44]
    contentval = dataEcho.decode().find('<')
    content = dataEcho.decode()[contentval:]

    
    
    if val == 'empty':
        f=open('cache.txt', 'w')
        f.write("Filename: "+filename+"\r\nLast-Modified: "+mod+"\r\nContents:"+content)
        f.close()
    else:
        f=open('cache.txt', 'r')
        check=f.read()
        f.close()
        if check.find(filename) == -1:
            f=open('cache.txt', 'a')
            f.write("Filename: "+filename+"\r\nLast-Modified: "+mod+"\r\nContents:"+content)
            f.close()
        else:
            f=open('cache.txt', 'r')
            checkl=f.readlines()
            f.close()
            f=open('cache.txt', 'r+')
            for line in checkl:
                if line.find(filename):
                    f.write("Filename: "+filename+"\r\nLast-Modified: "+mod+"\r\nContents:"+content)
                    break
            f.close()
            
            
            
    
# Close the client socket
clientSocket.close()
