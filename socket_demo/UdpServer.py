# coding:utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 12346))

print('Bind UDP on 12346 port.')

while True:
	data, addr = s.recvfrom(1024)
	print("Received from %s:%s." % addr)
	s.sendto(b'Hello, %s!' % data.decode('utf-8'), addr)