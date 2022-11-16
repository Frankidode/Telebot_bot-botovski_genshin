from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random as rn
from settings import Token
from phrases import *
from message_parsing import sms_otvetka

def memas(bot, update):
    bot.message.reply_photo(rn.choice(memasiki))

def start_sms(bot, update):
    print('Пользователь  написал start')
    bot.message.reply_text('Привет! Ты ввел команду start')
    '''
def sms_otvetka(bot, update):

    sms = bot.message.text
    if sms.lower()=='привет':
        print(bot.message)
        bot.message.reply_text(rn.choice(hello_bot)+', '+rn.choice(obrashenie))
    elif sms == 'бот':
        bot.message.reply_text('ЧЁ?')
    else:
        bot.message.reply_text('Я не понял ничего')
    '''

def main():
    my_bot = Updater(Token)
    my_bot.dispatcher.add_handler(CommandHandler('start', start_sms))
    my_bot.dispatcher.add_handler(CommandHandler('mem', memas))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, sms_otvetka))

    my_bot.start_polling() #проверяет наличие сообщений
    my_bot.idle() # бот работает, пока его не остановят

main()


