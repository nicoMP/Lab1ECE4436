import socket
import ssl 
print(ssl.OPENSSL_VERSION)
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
ctx = ssl.create_default_context()

# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = 'smtp-mail.outlook.com'

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, 587))
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')




# Send HELO command and print server response. 

heloCommand = 'EHLO www6.CheckTLS.com\r\n' 
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')
clientSocket.send('STARTTLS \r\n'.encode())
recv =clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')



# Send MAIL FROM command and print server response.s
 
# Fill in start'
mailFrom = 'MAIL FROM: <nick2000@live.ca>\r\n'
clientSocket.send('EHLO \r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
recv = clientSocket.recv(1024).decode()
print(recv)
recv = clientSocket.recv(1024).decode()
print(recv)

# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
#mailTO = 'RCPT TO:nick2000@live.ca'
#clientSocket.send(mailTO.encode())
#recv = clientSocket.recv(1024).decode()
#print(recv)
#if recv[:3] != '220':
#    print('220 reply not received from server.')

# Fill in end




# Send DATA command and print server response.

# Fill in start




# Fill in end




# Send message data.

# Fill in start




# Fill in end

# Message ends with a single period.

# Fill in start

# Fill in end




# Send QUIT command and get server response.

# Fill in start




# Fill in end
