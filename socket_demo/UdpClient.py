# coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Joel', b'Temo', b'Neo']:
	s.sendto(data, ('127.0.0.1', 12346))
	print(s.recv(1024).decode('utf-8'))

s.close()