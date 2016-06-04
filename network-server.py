#!/usr/bin/env python

import socket
import time

def server_quit():
	print('Server shutting down by remote command')

	conn.close()
	quit()

TCP_IP = '127.0.0.1'
TCP_PORT = 42626
BUFFER_SIZE = 4096  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while 1: #Chasing tails
	conn, addr = s.accept() #We are now accepting connections
	print('Connection address:', addr) #Wait, where did that come from??
	while 1: #Running in circles
		data = conn.recv(BUFFER_SIZE)
		if not data: break
		print("received data:", data.decode('utf-8')) #
		incoming = data.decode('utf-8')
		conn.send(data)  # This bit never sends....
	if incoming == "/exit":
		shutdown_message = 'Server shutting down'
		conn.send(shutdown_message.encode('utf-8'))
		time.sleep(1)
		server_quit()
	#And now, CAAAARDS
	if incoming == "[PlayingCard]":
		print('playing')
		cardid = 'CardID'
		conn.send(cardid.encode('utf-8'))
