import socket

# take the server name and port name

host = 'local host'
port = 8888

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect(('192.168.178.15', port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)

# repeat as long as message
# string are not empty
print(" Name: \n ID Number: \n Contact: \n Gender: \n Email: \n")

while msg:
        n_msg = input()
        s.send(n_msg.encode())
        id_msg = input()
        s.send(id_msg.encode())
        c_msg = input()
        s.send(c_msg.encode())
        g_msg = input()
        s.send(g_msg.encode())
        e_msg = input()
        s.send(e_msg.encode())

        print("Press 0 to submit")
        a = int(input())
        if (a == 0):
           break

print("SUBMITTED! Please wait at the counter for confirmation.")

noti = "Registration SUCCESS!"
s.send(noti.encode())

# disconnect the client
s.close()
