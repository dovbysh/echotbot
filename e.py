import telebot

# Вставьте сюда свой токен, полученный от BotFather
TOKEN = 'ВАШ_ТОКЕН'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой эхо-бот. Отправь мне что-нибудь.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

