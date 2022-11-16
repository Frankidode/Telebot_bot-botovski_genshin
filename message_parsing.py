from telegram.ext import Updater
import random as rn
from phrases import hello_bot, hello_sms, web_site, web_vk, bot_error, bot_error_pic

def hello(bot, update):
    bot.message.reply_text(f'{rn.choice(hello_bot)}, {bot.message.chat.first_name}! {hello_sms}')

def send_web(bot, update):
    bot.message.reply_text("Держите ссылочку на наш сайт: "+web_site)

def send_vk(bot, update):
    bot.message.reply_text("Держите ссылочку на нашу группу: "+web_vk)

def not_found_command(bot, update):
    bot.message.reply_photo(bot_error_pic, caption=bot_error)

def sms_otvetka(bot, update):
    text = [ t[:4] for t in bot.message.text.lower().split()]
    flag = 0
    if 'прив' in text or 'здра' in text:
        hello(bot, update)
        flag = 1
    if 'сайт' in text:
        send_web(bot, update)
        flag = 1
    if 'груп' in text or 'сооб' in text:
        send_vk(bot, update)
        flag = 1

    if flag==0:
        not_found_command(bot, update)


