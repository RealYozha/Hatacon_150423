import telebot
from telebot import types

token = '6122899991:AAFCwrbFAANH0pHMaQrdSy8lUfcWgjmn5X4'
bot = telebot.TeleBot(token)

questions =  [
              "0. Какой может быть максимальная длинна строки с Flake8?",
              "79", "79", "254", "139"
             ], [
              "1. Что обозначает переменная int?",
              "Целое число", "Целое число", "Параметр", "Строку"
             ], [
              "2. Как правильно задать переменной значение?",
              "x = 10", "10 = x", "x = 10", "x == 10"
             ], [
              "3. Что делает функция len()?",
              "Возвращает длинну строки", "Выдаёт случайное число", "Возвращает длинну строки", "Возвращает номер символа"
             ], [
              "4. Что делает функция break?",
              "Досрочно выходит из цикла", "Выдаёт случайное число", "Возвращает длинну строки", "Досрочно выходит из цикла"
             ], [
              "5. Что обозначает переменная str (string)?",
              "Строку", "Целое число", "Параметр", "Строку"
             ], [
              "6. Что обозначает переменная bool?",
              "Да/нет", "Да/нет", "Ничего", "Пустую строку"
             ], [
              "7. Укажите оператор ввода:",
              "input()", "input()", "print()", "int()"
             ], [
              "8. Как добавить модуль в программу?",
              "import library", "import library", "import: library", "import library.py"
             ]

@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    markup.add(item1)
    bot.send_message(message.chat.id,
                     text="Хотите начать?",
                     reply_markup=markup)

def get_question(i):
    keyboard = types.ReplyKeyboardMarkup()
    key_1 = types.KeyboardButton(text=questions[i][2])
    keyboard.add(key_1)
    key_2 = types.KeyboardButton(text=questions[i][3])
    keyboard.add(key_2)
    key_3 = types.KeyboardButton(text=questions[i][4])
    keyboard.add(key_3)
    questionText = questions[i][0]
    return questionText, keyboard

def check(i, txt):
    if txt == questions[i][1]:
        print('True')
        return False
    else:
        print('False! Compare', txt, 'with', questions[i][1])
        return True
    
@bot.message_handler(content_types=['text'])
def message_reply(message):
    i = 0
    score = 0
    if message.text == "Да":
        questionText, keyboard = get_question(i)
        bot.send_message(message.chat.id,
                                text=questionText,
                                reply_markup=keyboard)
    else:
        qId = message.id - 1
        nextQuestion = bot.forward_message(message.chat.id, message.chat.id, qId)
        nextI = int(nextQuestion.text[0])
        if check(nextI, message.text):
            return
        nextI += 1
        print(nextI)
        score += 1
        bot.delete_message(message.chat.id, nextQuestion.id)
        questionText, keyboard = get_question(nextI)
        bot.send_message(message.chat.id, questionText, reply_markup=keyboard)
    print('score =', score,'i =', i)
    if message.text == questions[i][1]:
        score =+ 1

bot.polling(non_stop=True, interval=0)

# RealYozha, 2023
