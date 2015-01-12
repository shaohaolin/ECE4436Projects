'''
Created on 2014年9月29日

@author: kurt
'''
from socket import * 
from datetime import datetime
from time import time

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #created a client side socket
clientSocket.settimeout(1)   # set the timeout at 1 second

counter = 0 #variable that tracks the sequence number
min = 0.0
avg = 0.0
max = 0.0
loss = 0 #variable that tracks the number of loss pkts

while (counter < 10):
    message = "Ping:"
    timeStart = datetime.now() #assign current time to a variable 
    try:
        message = message+ str(counter) +' '+ str(datetime.now())
        elapsed = (datetime.now()-timeStart).microseconds/1000
        avg += elapsed
        if counter==0:
                        min = elapsed
                        max = elapsed
        else:
            if min>elapsed :
                            min = elapsed
            else:
                if max<elapsed :
                            max = elapsed
        counter += 1
        clientSocket.sendto(bytes(message,"UTF-8"),(serverName,serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024) #receives msg from server
        print(modifiedMessage)
    
    except timeout:
        loss +=1
        print('*** Request Time Out. ***')


avg = avg/(10-loss)
lossPercent = loss*10
print('RTT is: Min:' + str(min) + 'ms Avg:'+str(avg) + 'ms Max:' + str(max)+'ms Packet Loss:' +str(lossPercent)+ '%')


clientSocket.close()