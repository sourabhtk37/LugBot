import telepot
import time
from pprint import pprint
from flask import Flask
import os

app=Flask(__name__)

if __name__ == '__main__':
        port=int(os.environ.get('PORT',5000))
        app.run(host='0.0.0.0',port=port)


bot=telepot.Bot("311260979:AAHLdVM2CoHi-Bg0GwWCFAgCmAB8Ad6vLZw")

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	#if msg['text'] == '/invite':
		#bot.sendMessage(chat_id,"Invite Who?")
	if msg['text'] == '/invitelink':
		bot.sendMessage(chat_id,"https://telegram.me/joinchat/DQQdYgqEmJF62rPE__9d_w")
	if msg['text'] == '/mailinglist':
		bot.sendMessage(chat_id,"http://frodo.hserus.net/mailman/listinfo/ilugd")
	print(msg)


bot.message_loop(handle)
while 1:
        pass

