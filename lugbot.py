# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import configparser
import logging
from telegram import ChatAction

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('bot.ini')


updater = Updater(token=config['BOT']['TOKEN'])
dispatcher = updater.dispatcher
help_text="""
[ x ] /invitelink  --> Prints the invite link to this group
[ x ] /twitter     --> Link to the ILUG-D Twitter
[ x ] /facebook    --> Facebook page of ILUG-D
[ x ] /mailinglist --> Link to the mailing list for ILUG-D
"""

def invitelink(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['invite_link'])

def twitter(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['twitter'])

def facebook(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['facebook'])

def mailinglist(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['mailing_list'])

def help(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=help_text,parse_mode='Markdown')


twitter_handler = CommandHandler('twitter',twitter)
invite_handler = CommandHandler('invitelink',invitelink)
facebook_handler = CommandHandler('facebook',facebook)
mailinglist_handler = CommandHandler('mailinglist',mailinglist)
help_handler = CommandHandler('help',help)

dispatcher.add_handler(twitter_handler)
dispatcher.add_handler(invite_handler)
dispatcher.add_handler(facebook_handler)
dispatcher.add_handler(mailinglist_handler)
dispatcher.add_handler(help_handler)


updater.start_polling()
updater.idle()
