import telebot
import random
from visa import visa_response

TOKEN = '667170954:AAGLG-nRBZc5TFYdgdNaVDg2fCvda2uDbs0'

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['text'])
# def echo_digits(message):
#     bot.reply_to(message, random.random())


@bot.message_handler(commands=['records'])
def echo_visa_record(message):
    bot.reply_to(message, visa_response())


bot.polling(timeout=60)
