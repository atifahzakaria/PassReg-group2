import socket

s = socket.socket()

port = 8888

s.connect(('192.168.178.15', port))

data = s.recv(1024)

s.send(b'Hi!');

print(data)

s.close()

