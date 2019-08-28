'''
Nishanth Gona
ng334
CS356-006
'''

#This code was written using socket api document on moodle
#What I used to time https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

import sys, time, struct
from socket import *

# Get the server hostname, port and data length as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
count = argv[3]

# Command line argument is a string, change the port and count into integer
port = int(port)
count = int(count)
data = 'X' * count # Initialize data to be sent
# Create UDP client socket. Note the use of SOCK_DGRAM
exceptioncounter = 0
clientsocket = socket(AF_INET, SOCK_DGRAM)

#Used this resource for settimeout https://docs.python.org/2/library/socket.html
clientsocket.settimeout(1)
while exceptioncounter!=3:
    # Sending data to server
    start = time.perf_counter()
    print("Sending data to " + host + ", " + str(port) + ": " + data + " (10 characters)")
    clientsocket.sendto(data.encode(),(host, port))
    try:
        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(count)
        # Display the server response as an output
        end = time.perf_counter()
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        #Close the client socket
        clientsocket.close()
        break
    #for excepting a timeout i used https://stackoverflow.com/questions/11865685/handling-a-timeout-error-in-python-sockets/11865993
    except timeout:
        print("message timed out")
        exceptioncounter = exceptioncounter+1
print("total run time:" + str(end-start))
 
