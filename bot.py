import telebot
from telebot import types
import requests
from decouple import config
from funcs_to_bot import *
import json
bot = telebot.TeleBot(config('BOT_KEY'))

users = {}
anket_counter = 0
def get_one_anket(ankets):
    get_one_anket.call_counter = 0
    one_anket = json.loads(ankets).pop(get_one_anket.call_counter)
    get_one_anket.call_counter += 1
    return one_anket

def pretty_anket(anket):
    first_name = anket['first_name']
    last_name = anket['last_name']
    sex = anket['sex']
    zodiac = anket['zodiac']
    age = anket['age']
    photo = anket['photo']
    return f'Имя: {first_name}\n Фамилия: {last_name}\n Пол: {sex}\n Возраст: {age}\n Фото: {photo}\n '


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, \nдля начала тебе в обязательном порядке нужно войти в свой аккаунт\nДля этого введи "Войти"\n(если ты еще не зарегистрирован, то можешь создать акканут по API: http://127.0.0.1:8000/account/auth/users/ ))')
    bot.send_message(message.chat.id,'Введи свои данные в следующем формате:\nexample_username\nexample_password')

@bot.message_handler(func=lambda message: True)
def authorize_user(message):
    global anket_counter
    username, password = message.text.split('\n')
    user = AuthUser(username, password)
    response = user.authenticate_user()
    bot.send_message(message.chat.id, response)
    users['user'] = user

    send_next_anket(message, user, anket_counter)

@bot.message_handler(func=lambda message: message.text.lower() == 'лайк')
def like_anket(message):
    global anket_counter
    user = users['user']
    send_next_anket(message, user, anket_counter)

@bot.message_handler(func=lambda message: message.text.lower() == 'еще')
def skip_anket(message):
    global anket_counter
    anket_counter += 1
    user = users['user']
    send_next_anket(message, user, anket_counter)

def send_next_anket(message, user, anket_counter):
    if anket_counter < len(user.get_ankets()):
        current_anket = user.get_ankets()[anket_counter]
        bot.send_message(message.chat.id, current_anket)
    else:
        # Если анкеты закончились, отправляем соответствующее сообщение
        bot.send_message(message.chat.id, 'Анкеты закончились')


# @bot.message_handler(func=lambda message: True)
# def get_user_data(message):
#     user_data = message.text
#     username, password = user_data.split('\n')
#     user = AuthUser(username, password)
#     auth_result = user.authenticate_user()
#     users[0] = user
#     bot.send_message(message.chat.id, auth_result)
#     keyboard_to_ok = telebot.types.InlineKeyboardMarkup()
#     button = telebot.types.InlineKeyboardButton(text="хорошо", callback_data="ok")
#     keyboard_to_ok.add(button)
#     bot.send_message(message.chat.id,'Вам будет отправляться по одной анкете по системе рекомендаций\n',reply_markup=keyboard_to_ok)

@bot.callback_query_handler(func=lambda call: True)
def call_ok(call):
    if call.data == "ok":
        bot.send_message(call.message.chat.id, "Поехали")
        ankets = users[0].get_ankets()
        bot.send_message(call.message.chat.id, pretty_anket(get_one_anket(ankets)))


    













bot.polling()