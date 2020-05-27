import socket
host = socket.gethostname()
port = 12345
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((host,port))

message = "Hello this is client"

s.sendall(message.encode("UTF-8"))
data = s.recv(1024)
print(data.decode("UTF-8"))
s.close()
