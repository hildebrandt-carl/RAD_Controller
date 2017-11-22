import socket
sock = socket.socket()
sock.connect(('160.119.248.176', 4242))
sock.send("Hello from python")
print sock.recv(256)
sock.close()