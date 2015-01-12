'''
Created on 2014年11月15日

@author: kurt
'''
import socket
import time

Any = '0.0.0.0'
sendPort = 1501
multicast_addr = '224.168.2.9'
multicast_port = 1600

msg = "Multicasting Assignment ECE 4436 from Serve 1"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.bind((Any,sendPort))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
while 1:
    time.sleep(3)
    sock.sendto(msg.encode(encoding='utf_8'),(multicast_addr,multicast_port))
    print('Server 1 : multicast packet is sent now')