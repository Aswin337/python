import socket
s=socket.socket()
s.connect(("localhost",9006))
print(s.recv(1024).decode())
