import socket

host = socket.gethostname()
port = 1234
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(3)

print('wating..')
conn,addr = s.accept()
print("Connected : ", addr)

while True:
	data = conn.recv(1024)
	data = data.decode('utf-8')
	d = [x for x in data.split(",")]
	result = 0
	for num in d:
		if(num.isdigit()):
			result += int(num)
	d = str(result)
	if not data: break
	conn.sendall(d.encode('utf-8'))

conn.close()