import irclib
import re
import random
class doge:
    def __init__(self):
	self.responses = []
	self.dogeFile = open("responses.txt","r")
	self.responses = dogeFile.read().splitlines()
	self.dogeFile.close()
    def on_pubmsg(self, nick, connection, event):
        message = event.arguments()[0]
	if("doge" in message):
		connection.privmsg(event.target(), self.responses[random.randint(0,len(self.responses)-1)])
