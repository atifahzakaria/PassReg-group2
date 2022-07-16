import socket

# take the server name and port name
host = 'local host'
port = 8888

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
c, addr = s.accept()

# display client address
print("CONNECTION FROM:", str(addr))

# send message to the client after
# encoding into binary string
c.send(b"Welcome! Let's register your passport HERE!\nKindly fill in your information below: \n")

#receive reply from client
c_rep = c.recv(1024)
print("Name: ", c_rep.decode())
c_rep = c.recv(1024)
print("ID Number: ", c_rep.decode())
c_rep = c.recv(1024)
print("Contact: ", c_rep.decode())
c_rep = c.recv(1024)
print("Gender: ", c_rep.decode())
c_rep = c.recv(1024)
print("Email: ", c_rep.decode())

c_noti = c.recv(1024)
print(c_noti.decode())
# disconnect the server
c.close()
