import telebot


token = '6147473906:AAG2LA74-m3v6WNRAOIXZs4GYrdvPuCTeYg'
bot = telebot.Telebot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


bot.infinity_poling()
