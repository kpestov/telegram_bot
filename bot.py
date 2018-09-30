import telebot
from visa import visa_response

TOKEN = '667170954:AAGLG-nRBZc5TFYdgdNaVDg2fCvda2uDbs0'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    info = '''
    I can help you to manage different routines.
    
You can control me by sending these commands:
    
/interview - know free dates to apply for visa
    '''
    bot.reply_to(message, info)


@bot.message_handler(commands=['interview'])
def echo_visa_record(message):
    bot.reply_to(message, visa_response())


bot.polling(timeout=60)
