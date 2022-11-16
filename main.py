from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from settings import Token, hello_bot, obrashenie
import random as rn

def memas(bot, update):git rm --cached
    bot.message.reply_photo('https://pbs.twimg.com/media/EysbMQbWgAAi5bG.jpg')

def start_sms(bot, update):
    print('Пользователь  написал start')
    bot.message.reply_text('Привет! Ты ввел команду start')

def sms_otvetka(bot, update):
    sms = bot.message.text
    if sms.lower()=='привет':

        bot.message.reply_text(rn.choice(hello_bot)+', '+rn.choice(obrashenie))
    elif sms == 'бот':
        bot.message.reply_text('ЧЁ?')
    else:
        bot.message.reply_text('Я не понял ничего')

def main():
    my_bot = Updater(Token)
    my_bot.dispatcher.add_handler(CommandHandler('start', start_sms))
    my_bot.dispatcher.add_handler(CommandHandler('mem', memas))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, sms_otvetka))

    my_bot.start_polling() #проверяет наличие сообщений
    my_bot.idle() # бот работает, пока его не остановят

main()


