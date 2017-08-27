# coding:utf-8

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 12345))

print('recv : ' + s.recv(1024).decode('utf-8'))

s.send(b'Good, this is a client.')

print('recv : ' + s.recv(1024).decode('utf-8'))

s.send(b'exit')

s.close()