import telepot
from flask import Flask
import requests
import time
app = Flask(__name__)


@app.route('/')
def home():
    return "bruh,this is the shit."


invite_link = "https://telegram.me/joinchat/DQQdYgqEmJF62rPE__9d_w"
mailing_list = "http://frodo.hserus.net/mailman/listinfo/ilugd"

if __name__ == '__main__':

    bot = telepot.Bot("311260979:AAHLdVM2CoHi-Bg0GwWCFAgCmAB8Ad6vLZw")

    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        if msg['text'] == '/invitelink':
            bot.sendMessage(chat_id, invite_link)
        if msg['text'] == '/mailinglist':
            bot.sendMessage(chat_id, mailing_list)

    bot.message_loop(handle)
    while 1:
        time.sleep(30)
        r = requests.get("http://glacial-plateau-17952.herokuapp.com/")
        print(r.text)
