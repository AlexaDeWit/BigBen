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
        #DEPRECATED
	#if message == ".shorten":
	#	if(len(self.lastUrls)>0):
	#		connection.privmsg(event.target(), self.shortenURL(self.lastUrls[0]))
	
	
	#Continually watches chat for URLS, keeping the last one posted in memory
	if ("http://" in message or "https://" in message):
		self.lastUrls = re.findall(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+',message)
	#output a shortened version of the most recent url
	#because of the implementation of this function, .shorten url will store the url 
	#BEFORE the shorten logic, thus allowing you to do it in a single statement
	if message.startswith(".shorten"):
		url = message[9:]
		connection.privmsg(event.target(), self.shortenURL(url))
