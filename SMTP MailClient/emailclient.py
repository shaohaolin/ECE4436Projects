from socket import *
import ssl
import base64

# Setup messages

msg = "\r\n Ryan, I am so hungry.Shiiiit." 	# email body
endmsg = "\r\n.\r\n"					# end of body

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"# fill in start   # fill in end			
port = 587

clientSocket=socket(AF_INET,SOCK_STREAM) #establish a TCP connection with mailserver
clientSocket.connect((mailserver,port))

#Read server response
recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != "220":
    print ('220 reply not received from server.')

heloCommand = "HELO Alice\r\n"
clientSocket.send(bytes(heloCommand,'utf-8'))
recv1 = clientSocket.recv(1024)
print (recv1),
if recv1[:3] != '250': 
    print ('250 reply not received from server.')
    
# Send STARTTLS command to server and print server response
command = "STARTTLS\r\n"
clientSocket.send(bytes(command, 'utf-8'))

recv1 = clientSocket.recv(1024)
print (recv1)
if recv[:3] != '220':
    print ('220 reply not received from server.')

#Wrap the socket with SSL wrapper
tls_clientSocket = ssl.wrap_socket(clientSocket)

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
tls_clientSocket.send(bytes(heloCommand,'utf-8'))
recv1 = tls_clientSocket.recv(1024)
print (recv1),
if recv1[:3] != '250': 
    print ('250 reply not received from server.')
 
# SEND AUTH LOGIN command and Base64 encoded username
command = "AUTH LOGIN \r\n"
tls_clientSocket.send(bytes(command,'utf-8'))

recv1 = tls_clientSocket.recv(1024)
print (recv1)

#Authenticate with User/Password and print server response.
tls_clientSocket.send(base64.b64encode(bytes('shaohaolinca@gmail.com','utf-8')))
tls_clientSocket.send(bytes('\r\n','utf-8'))
tls_clientSocket.send(base64.b64encode(bytes('password','utf-8')))
tls_clientSocket.send(bytes('\r\n','utf-8'))
recv = tls_clientSocket.recv(1024)
print (recv),
if recv[:3] != "220":
    print ('220 Login: reply not received from server.')
         
# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL From: <shaohaolinca@gmail.com>\r\n'
tls_clientSocket.send(bytes(mailFromCommand,'utf-8'))
recv2 = tls_clientSocket.recv(1024)
print (recv2)

if recv2[:3] != "250":
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. RCPT TO is recipient, like where the email goes to
rcptToCommand = "RCPT TO: <ryan.toth@live.com>\r\n"
tls_clientSocket.send(bytes(rcptToCommand,'utf-8'))
recv3 = tls_clientSocket.recv(1024)
print (recv3)

if recv3[:3] !="250":
    print ('250 reply not received from server.')
    
# Send DATA command and print server response.
dataCommand = "DATA\r\n"
tls_clientSocket.send(bytes(dataCommand,'utf-8'))
recv4 = tls_clientSocket.recv(1024)
print (recv4)

if recv4[:3] != '250':
    print ('Data:250 reply not received from server.')

# Send message subject, body and data
tls_clientSocket.send(bytes(msg,'utf-8'))

# Message ends with a single period.
tls_clientSocket.send(bytes(endmsg,'utf-8'))

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
tls_clientSocket.send(bytes(quitCommand,'utf-8'))
recv5 =tls_clientSocket.recv(1024)
print (recv5)

if recv5[:3] != '221':
    print ('Quit:221 reply not received from server.')
