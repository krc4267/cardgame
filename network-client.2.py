#!/usr/bin/env python

import socket


<<<<<<< HEAD
TCP_IP = '192.168.1.78'
TCP_PORT = 42626
=======
TCP_IP = '99.38.160.240'
TCP_PORT = 5005
>>>>>>> 8da939f8291ae1b00d1d8bbb1ec2a861029c77d4
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
