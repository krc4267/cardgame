import socket #imports module allowing connection to IRC
import threading #imports module allowing timing functions
import sys


#sets variables for connection to twitch chat
bot_owner = 'krc4267'
nick = 'cardclient'
channel = '#krc4267'
server = 'irc.freenode.net'
#password = ''

queue = 0 #sets variable for anti-spam queue functionality

irc = socket.socket()
irc.connect((server, 6667)) #connects to the server

#sends variables for connection to twitch chat
#irc.send('PASS ' + password + '\r\n'.encode('utf-8'))
irc.send('USER ' + nick + ' 0 * :' + bot_owner + '\r\n'.encode('utf-8'))
irc.send('NICK ' + nick + '\r\n'.encode('utf-8'))
irc.send('JOIN ' + channel + '\r\n'.encode('utf-8')) 

def message(msg): #function for sending messages to the IRC chat
    global queue
    queue = queue + 1
    print(queue)
    if queue < 20: #ensures does not send >20 msgs per 30 seconds.
        irc.send('PRIVMSG ' + channel + ' :' + msg + '\r\n'.encode('utf-8'))
    else:
        print('Message deleted')

def queuetimer(): #function for resetting the queue every 30 seconds
    global queue
    print('queue reset')
    queue = 0
    threading.Timer(30,queuetimer).start()
queuetimer()

while True:
    data = irc.recv(1204) #gets output from IRC server
    user = data.split(':')[1]
    user = user.split('!')[0] #determines the sender of the messages
    print(data)

    if data.find('PING') != -1:
        irc.send(data.replace('PING', 'PONG').encode('utf-8')) #responds to PINGS from the server
    if data.find('!test') != -1: #!test command
        message('Hi')
