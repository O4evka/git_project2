import telebot

bot = telebot.TeleBot("6147473906:AAG2LA74-m3v6WNRAOIXZs4GYrdvPuCTeYg")

questions = [
    "Какая у тебя шерсть?",
    "Какой у тебя окрас?",
    "Какого размера у тебя уши?",
    "Какие ты любишь игрушки?",
    "Как ты общаешься с другими котами?",
]

answers = [
    ["Длинная", "Короткая", "Средняя"],
    ["Белый", "Черный", "Полосатый"],
    ["Большие", "Маленькие", "Незнаю :D"],
    ["Мячики", "Мышки", "Что угодно"],
    ["Агрессивно", "Дружелюбно", "Не общаюсь"],
]

results = ["Персидский кот", "Сиамский кот", "Мейн-кун"]

count = -1

ans = [0, 0, 0]


@bot.message_handler(commands=["start"])
def start_test(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Я помогу тебе узнать, какой ты кот. Я задам тебе пять во"
        f"просов, а ты на них ответишь. Готов начать? Напиши /test"
    )


@bot.message_handler(commands=["test"])
def run_test(message):
    global count, ans
    count = 0
    ans = [0, 0, 0]
    markup = telebot.types.ReplyKeyboardMarkup()
    for answer in answers[0]:
        markup.add(telebot.types.KeyboardButton(answer))
    bot.send_message(message.chat.id, questions[count], reply_markup=markup)


@bot.message_handler()
def process_answer_step(message):
    global count
    if count != -1 and message.text.strip() in answers[count]:
        ans[answers[count].index(message.text)] += 1
        count += 1
        if count == len(questions):
            idi = 0
            for i in range(len(ans)):
                if ans[i] > ans[idi]:
                    idi = i
            result = results[idi]
            c = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, f"Ты - {result}. Поздравляю!", reply_markup=c)
            count = -1
        else:
            markup = telebot.types.ReplyKeyboardMarkup()
            for answer in answers[count]:
                markup.add(telebot.types.KeyboardButton(answer))
            bot.send_message(message.chat.id, questions[count], reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Не понимаю. Напиши /start для начала теста, или'
                                          ', если уже проходишь, нажми на кнопку для ответа.')


bot.polling()
