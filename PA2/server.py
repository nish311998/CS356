'''
Nishanth Gona
ng334
CS356-006
'''

#This code was written using the socket api document on moodle

import sys, struct
from socket import *
import random 
# Get the server hostname, port and data length as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
serverIP = host
serverPort = int(port)
dataLen = 1000000
# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print('The server is ready to receive on port: ' + str(serverPort))
# loop forever listening for incoming datagram messages
while True:
    # Receive and print the client data from "data" socket
    
    data, address = serverSocket.recvfrom(dataLen)
    dataval = struct.unpack("!II", data)
    val = random.randint(0,10)
    if val>=4:
        print("Responding to a ping request with sequence number " + str(dataval[1]))
        datamsg = struct.pack("!II", 2, dataval[1])
        serverSocket.sendto(datamsg,address)
    else:
        print("Message with sequence number " + str(dataval[1]) + " dropped")
