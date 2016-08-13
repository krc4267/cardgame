import socket
import os.path

#Begin config area
#These variables are used to control various aspects of the server
#And will probably be moved to a proper config file... someday.

storedserver='/home/krc/cardserver4.conf'
serverport=6667
#storedserver='C:\\Users\\Cruxien\\Cardgame\\cardgame'

#End config area

global irc


def setupirc(): #This function should create/recreate the file which is storing the address of the irc server to connect to
	print('No stored server has been found.')
	f = open(storedserver, 'w')
	f.write(input('Please specify the address of an IRC server which will host the game: '))
	f.close()
	connect()

if os.path.exists(storedserver):
	print('Reading stored server from', storedserver)
	f = open(storedserver) #Opens the file which is storing our server address
	connect_to = f.readline() #Reads (hopefully...) the address for the server
	f.close() #Close the file
	print('Now connecting to', connect_to) #Print what we're connecting to
	global irc
	irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	irc.connect((connect_to, serverport))
	irc.send('NICK CardServerrn'.encode('utf-8'))
	irc.send('USER CardServer CardServer CardServer :Card Serverrn'.encode('utf-8'))
	irc.send('JOIN #cardslobbyrn'.encode('utf-8'))
	irc.send('PRIVMSG #cardslobby :Can you hear me??rn'.encode('utf-8'))
else:
	setupirc()

#Thus begins the main server loop (oh dear...)

while True:
	data = irc.recv(4096)
	if data.find('PING'.encode('utf-8')) != -1:
		irc.send('PONG'.encode('utf-8') + data.split() [1] + 'rn'.encode('[utf-8'))
	
