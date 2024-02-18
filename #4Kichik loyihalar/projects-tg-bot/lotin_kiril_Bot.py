"""
@author: Abduljabbor
"""
from transliterate import to_cyrillic,to_latin
import telebot

TOKEN="bu yerga bot tokkeni joylanadi"
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, Hush kelibsiz")
    


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    
    javob=lambda mgs:to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    bot.reply_to(message, javob(msg))

bot.infinity_polling()