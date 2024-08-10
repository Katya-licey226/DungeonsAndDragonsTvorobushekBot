import telebot
from config import botkey
bot = telebot.TeleBot(botkey)
@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.send_message(message.chat.id, 'Привет❗️')
@bot.message_handler(commands=['help'])
def handle_message(message):
    bot.send_message(message.chat.id, '😀 Я - тестовый бот❗️')
bot.polling()