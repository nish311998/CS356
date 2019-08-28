'''
Nishanth Gona
ng334
CS356-006
'''

#This code was written using socket api doc on moodle
import sys
from socket import *
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
    print("Receive data from client " + address[0] + ", " + str(address[1]) + ": " + data.decode())
'''
    # Echo back to client
    print("Sending data to client " + address[0] + ", " + str(address[1]) + ": " + data.decode())
    serverSocket.sendto(data,address)
    
'''
