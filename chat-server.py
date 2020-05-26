import socket

host = socket.gethostname()
port = 5429
s = socket.socket()
s.bind((host,port))
s.listen(3)

print('wating..')
conn,addr = s.accept()
print("Connected : ", addr)

while True:
	data = conn.recv(1024)
	data = data.decode('utf-8')
	d = str(sum([int(x.strip()) for x in data.split(",")]))


	if not data: break
	conn.sendall(d.encode('utf-8'))

conn.close()