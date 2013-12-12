import random
class doge:
    def on_pubmsg(self, nick, connection, event):
        message = event.arguments()[0]
        source = event.source().split('!')[0]

	if "doge" in message:
		fortunestxt = open("modules/pubmsg/doge", 'r')
		fortuneslist = fortunestxt.read().splitlines()
		response = random.choice(fortuneslist)
		connection.privmsg(event.target(), response)