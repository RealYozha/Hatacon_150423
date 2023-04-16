import telebot
from telebot import types
from time import sleep

token = '6122930605:AAExT_6n1EtpiUgPwAN4YOeXveEBnxCZnuA'
bot = telebot.TeleBot(token)

questions = [
             [
              "Какой может быть максимальная длинна строки с Flake8?",
              "79", "79", "254", "139"
             ],
             [
              "Что обозначает переменная int?",
              "Целое число",
              "Целое число",
              "Параметр",
              "Строку"
             ],
             [
              "Как правильно задать переменной значение?",
              "x = 10",
              "10 = x",
              "x = 10",
              "x == 10"
             ],
             [
              "Что делает функция len()?",
              "Возвращает длинну строки",
              "Выдаёт случайное число",
              "Возвращает длинну строки",
              "Возвращает номер символа"
             ],
             [
              "Что делает функция break?",
              "Досрочно выходит из цикла",
              "Выдаёт случайное число",
              "Возвращает длинну строки",
              "Досрочно выходит из цикла"
             ],
             [
              "Что обозначает переменная str (string)?",
              "Строку",
              "Целое число",
              "Параметр",
              "Строку"
             ],
             [
              "Что обозначает переменная bool?",
              "Да/нет",
              "Да/нет",
              "Ничего",
              "Пустую строку"
             ],
             [
              "Укажите оператор ввода:",
              "input()",
              "input()",
              "print()",
              "int()"
             ],
             [
              "Укажите оператор ввода:",
              "input()",
              "input()",
              "print()",
              "int()"
             ],
             [
              "Как добавить модуль в программу?",
              "import library",
              "import library",
              "import: library",
              "import library.py"
             ],
             [
              "Как добавить модуль в программу?",
              "import library",
              "import library",
              "import: library",
              "import library.py"
             ]
            ]


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    markup.add(item1)
    bot.send_message(message.chat.id,
                     text="Хотите начать?",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Да":
        bot.send_message(message.chat.id,
                         "Начинаем! На каждый вопрос у вас есть 7 секунд.")
        score = 0
        for i in range(len(questions)):
            keyboard = types.ReplyKeyboardMarkup()
            key_1 = types.KeyboardButton(text=questions[i][2])
            keyboard.add(key_1)
            key_2 = types.KeyboardButton(text=questions[i][3])
            keyboard.add(key_2)
            key_3 = types.KeyboardButton(text=questions[i][4])
            keyboard.add(key_3)
            bot.send_message(message.chat.id,
                             text=questions[i][0],
                             reply_markup=keyboard)
            sleep(7)
            if message.text == questions[i][1]:
                score = score + 1
        text = f"Ваши баллы: {score}"
        bot.send_message(message.chat.id, text=text)


bot.polling(non_stop=True, interval=0)

# RealYozha, 2023
