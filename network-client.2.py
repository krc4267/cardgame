#!/usr/bin/env python

import socket

TCP_IP = input('Input the IP to connect to: ')
TCP_PORT = 42626
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

while 1:
	MESSAGE = input('Cardgame-0.1>:' )
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE.encode('utf-8'))
	data = s.recv(BUFFER_SIZE)
	s.close()
	print("received data:", data)
