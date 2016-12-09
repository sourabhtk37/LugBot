import telepot
import time
from pprint import pprint

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
	print('hmmm')