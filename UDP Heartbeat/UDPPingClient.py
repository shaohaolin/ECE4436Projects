'''
Created on 2014年10月1日

@author: kurt
'''
from socket import *
from datetime import *
import time
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #create a client side socket
clientSocket.bind((serverName,49765))

seq = 0 # sequence number
print(' ===== UDP Heartbeat Client ====')
print('Sending heartbeat to server every 3 seconds...')

while True:
    try:
        message = str(seq)
        clientSocket.sendto(bytes(message,'UTF-8'),(serverName,serverPort)) # Attach server name, port to message; send into socket
        seq += 1
        time.sleep(3)
    except timeout:
        print("Time out!")
        break

clientSocket.close()



