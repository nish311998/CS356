'''
Nishanth Gona
ng334
CS356-006
'''

import sys, os, os.path
import datetime, time
from socket import *


argv = sys.argv
serverIP = argv[1]
serverPort = argv[2]
dataLen = 100000

# Create a TCP "welcoming" socket. Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind((serverIP, int(serverPort)))
# Listen for incoming connection requests
serverSocket.listen(1)
#print('The server is ready to receive on port: ' + str(serverPort))

# loop forever listening for incoming connection requests on "welcoming" soecket
while True:
    # Accept incoming connection requests, and allocate a new socket for data communication
    connectionSocket, address = serverSocket.accept()
    #print("Socket created for client " + address[0] + ", " + str(address[1]))
    # Receive and print the client data in bytes from "data" socket
    data = connectionSocket.recv(dataLen).decode()
    print("HTTP Request:\r\n"+data)

    #HTTP GET Response
    
    #get filename
    index1 = data.find('/')
    index2 = data.find('.')
    filename = data[index1+1:index2+5]
    exists = os.path.isfile(filename) #check for file https://therenegadecoder.com/code/how-to-check-if-a-file-exists-in-python/
    if exists:
        if data.find("If-Modified") == -1:

            #use GET Response
            
            #get curr date using resources from document
            t = datetime.datetime.now(datetime.timezone.utc)
            date = t.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n") #Don't know if this is the right notation for all of these

            #get modiified date
            secs = os.path.getmtime(filename)
            t = time.gmtime(secs)
            mod = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
            

            #read file
            f=open(filename, 'r')
            content = f.read()
            length=len(content)
            f.close()
            
            data="HTTP/1.1 200 OK\r\nDate: "+date+"Last-Modified: "+mod+"Content-Length: "+str(length)+"\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"+content

           
            
        else:
            #use conditonal GET response
            #get modiified date using resources from document
            
            secs = os.path.getmtime(filename)
            t = time.gmtime(secs)
            mod = time.strftime("%a, %d %b %Y %H:%M:%S GMT", t)

            t = datetime.datetime.now(datetime.timezone.utc)
            date = t.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n")

            val = data.find('If-Modified')
            datemod = data[val+19:val+48]

            if mod == datemod:
                data = "HTTP/1.1 304 Not Modified\r\nDate: "+date+"\r\n"
            else:
                
                #read file
                f=open(filename, 'r')
                content = f.read()
                length=len(content)
                f.close()
                data="HTTP/1.1 200 OK\r\nDate: "+date+"Last-Modified: "+mod+"\r\n"+"Content-Length: "+str(length)+"\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"+content


    else:
        t = datetime.datetime.now(datetime.timezone.utc)
        date = t.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n")
        data="HTTP/1.1 404 Not Found\r\nDate: "+date+"\r\n"

    # Echo back to client
    connectionSocket.send(data.encode())
    connectionSocket.close()
