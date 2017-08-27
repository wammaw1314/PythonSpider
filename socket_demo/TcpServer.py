# coding:utf-8
import socket
import threading
import time

def dealClient(sk, addr):
	# 接收传来的数据，并发送给对方数据
	print('Accept new connection from %s:%s!' % addr)
	sk.send(b'Hello, this is server.')
	while True:
		data = sk.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		print 'recv: %s!' % data.decode('utf-8')
		sk.send(('Loop Send: %s.' % data.decode('utf-8')).encode('utf-8'))

	sk.close()
	print('Connection from %s:%s closed!' % addr)

if __name__ == '__main__':
	# 创建一个基于IPv4和TCP协议的Socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('127.0.0.1', 12345))
	s.listen(5)
	print('Waiting for connection...')
	while True:
		sk, addr = s.accept()
		#创建新线程来处理TCP连接
		t = threading.Thread(target=dealClient, args=(sk,addr))
		t.start()