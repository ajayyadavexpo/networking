import socket
host = socket.gethostname()
port = 12345
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(3)
print("Wating ... ")
conn,addr = s.accept()
print("Connected : ",addr)



while True:
	data = conn.recv(1024)
	data = data.decode("UTF-8")
	if not data:
		break
	else:
		print(data)
	conn.sendall(data.encode("UTF-8"))

conn.close()
	