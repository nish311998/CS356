'''
Nishanth Gona
ng334
CS356-006
'''

#This code was written using socket api document on moodle
#What I used to time https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution

import sys, time, struct
from socket import *


#ping variables
sent=10
received=0
endarr=[]
# Get the server hostname, port and data length as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]

# Command line argument is a string, change the port
port = int(port)
 
# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket(AF_INET, SOCK_DGRAM)

sequence = 1
#Used this resource for settimeout https://docs.python.org/2/library/socket.html
clientsocket.settimeout(1)
print("Pinging " + host + ' '+ str(port))
while sequence!=11:
    # Sending data to server
    datamsg = struct.pack("!II", 1, sequence)
    start = time.perf_counter()
    clientsocket.sendto(datamsg,(host, port))
    try:
        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(8)
        end = time.perf_counter()
        received = received+1
        dataval = struct.unpack("!II", dataEcho)
        # Display the server response as an output
        print("Ping message number " + str(dataval[1]) + " RTT: " + str(end-start) + " secs")
        endarr.append(end-start)
    #for excepting a timeout i used https://stackoverflow.com/questions/11865685/handling-a-timeout-error-in-python-sockets/11865993
    except timeout:
        print("Ping message number " + str(sequence) + " timed out")
    sequence=sequence+1

#Close the client socket
print("Packets sent:" + str(sent))
print("Packets received:" + str(received))
lost = ((sent - received)/sent)*100
print("Lost percentage:" + str(lost))
min = 1000000
max=-100000
avg = 0
for i in endarr:
    if i<min:
        min = i
    elif i>max:
        max = i
    avg = avg + i
avg = avg/len(endarr)
print("Min:" + str(min) + " secs")
print("Max:" + str(max) + " secs")
print("Avg:" + str(avg) + " secs")
clientsocket.close()
         
