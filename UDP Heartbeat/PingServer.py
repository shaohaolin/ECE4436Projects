# We will need the following module to generate randomized lost packets 
import random 
from socket import * 
import time 
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('127.0.0.1', 12000))
serverSocket.settimeout(5)

print(' ===== UDP Heartbeat Server =====')
print( 'Waiting to hear client heartbeats (5 sec timeout)...')
print("")
print("")
bufferMsg,address = serverSocket.recvfrom(1024)
print(" * * * client at: " + str(address) +" is online * * *")

t0 = time.time()
while True: 
    try:
# Receive the client packet along with the address it is coming from 
        message, address = serverSocket.recvfrom(1024) 
        #receMsg = message.decode('UTF-8') #decode message into string
        #receMsg.split(" ")
# If rand is less is than 4, we consider the packet lost and do not respond
        #if rand < 4:
    # print("packet has been lost!")
               # break
                #continue 
        # Otherwise, the server responds
        print ("SequenceNo.:"+str(message)+"("+str(round(time.time()-t0,2))+") s since last packet")
        t0 = time.time()
        serverSocket.sendto(message, address)
    except timeout:
                print(" Client at " + str(address) + "went OFFLINE")
                serverSocket.settimeout(None)