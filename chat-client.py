import socket
host = socket.gethostname()
port = 5420
s = socket.socket()

s.connect((host,port))
message = str(5)+','+str(6)

s.sendall(message.encode('utf-8'))
data = s.recv(1024)
print(data)
s.close()