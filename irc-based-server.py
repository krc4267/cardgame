import socket
import os.path

#Begin config area
#These variables are used to control various aspects of the server
#And will probably be moved to a proper config file... someday.

storedserver='/home/krc/cardserver.conf'

#End config area

def connect(): #Connects to specified IRC server
	print('Reading stored server from', storedserver)
	f = open(storedserver) #Opens the file which is storing our server address
	connect_to = f.readline() #Reads (hopefully...) the address from the server
	f.close() #Close the file
	print('Now connecting to', connect_to)

def setupirc(): #This function should create/recreate the file which is storing the address of the irc server to connect to
	print('No stored server has been found.')
	f = open(storedserver, 'w')
	f.write(input('Please specify the address of an IRC server which will host the game: '))
	f.close()
	connect()

if os.path.exists(storedserver):
	connect()
else:
	setupirc()
	
