'''
Created on 2014年11月15日

@author: kurt
'''
import socket
import time
Any = '0.0.0.0'
multicast_addr = '224.168.2.9'
multicast_port = 1600

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((Any,multicast_port))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
status = sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,socket.inet_aton(multicast_addr)+socket.inet_aton(Any))

sock.setblocking(0)
ts=time.time()
while 1:
    try:
        data,addr = sock.recvfrom(1024)
    except socket.error:
        pass
    else:
        print("Client 1 : Data Received from:", addr)
        print("and the Received Data is: ",data)