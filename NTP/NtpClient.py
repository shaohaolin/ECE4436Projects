import socket
import struct
import sys
import time
NTP_SERVER = 'pool.ntp.org' 
TIME1970 = 2208988800

def sntp_client():
    port = 123
    buf = 1024
    address = (NTP_SERVER,port)
    data = '\x1b' + 47 * '\0'
    
    # connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    client.sendto(data.encode('utf-8'),address)
    data, address = client.recvfrom(buf)
     
    
    if data:
        print ('Response received from:', address)
        
        t = struct.unpack( '!12I', data )[10]
        t -= TIME1970
        print ('\tTime=%s' % time.ctime(t))
if __name__ == '__main__':
    sntp_client()
