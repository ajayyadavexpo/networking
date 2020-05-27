import socket
host = socket.gethostname()
port = 1234
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((host,port))
message = '5'+','+'6'

s.sendall(message.encode('utf-8'))
data = s.recv(1024)
print(data)
s.close()