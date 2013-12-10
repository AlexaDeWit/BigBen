import irclib
import urllib
import BeautifulSoup
import re

class shorten:
    def __init__(self):
	self.messageList = []
	self.lastUrls = []

    def shortenURL(self, url):
	returnMessage = ""
	try:
		open_Url = urllib.urlopen("http://is.gd/create.php?format=simple&url=" + url)
		read_Content = str(BeautifulSoup.BeautifulSoup(open_Url.read()))
		returnMessage= "Shortened url: " + read_Content
	except:
		returnMessage = "Invalid url"
	return returnMessage

    def on_pubmsg(self, nick, connection, event):
        message = event.arguments()[0]
	#Scans each incoming message for urls, storing the most recent
	#Allws compounding with .shorten because the url will be parsed and stored before .shorten is
	#technically stores all the urls from a message(incase of multiple) but the response will only
	#be of the first url in the most recent message
	if ("http://" in message or "https://" in message):
		self.lastUrls = re.findall(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+',message)
	#responds to a user beginning a message with .shorten and responds to the request with the first stored url in chat
	if message == ".shorten":
		if(len(self.lastUrls)>0):
			connection.privmsg(event.target(), self.shortenURL(self.lastUrls[0]))
	#DEPRECATED
	#elif message.startswith(".shorten"):
	#	url = message[9:]
	#	connection.privmsg(event.target(), self.shortenURL(url))
	
