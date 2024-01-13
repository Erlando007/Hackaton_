import telebot
from telebot import types
import requests
from decouple import config
from funcs_to_bot import *
import json
bot = telebot.TeleBot(config('BOT_KEY'))

users = {}



def pretty_anket(anket):
    first_name = anket['first_name']
    last_name = anket['last_name']
    sex = anket['sex']
    zodiac = anket['zodiac']
    age = anket['age']
    photo = anket['photo']
    height = anket['height']
    return f'Фото: {photo}\n Имя: {first_name}\n Фамилия: {last_name}\n Пол: {sex}\n Возраст: {age}\n Рост: {height}'


def send_next_anket(message, ankets, anket_counter):
    current_anket = ankets[anket_counter]
    response = pretty_anket(current_anket)
    markup = types.InlineKeyboardMarkup()
    id = current_anket['id']
    like_data = json.dumps({'option': 'like', 'anket_id': id})
    skip_data = json.dumps({'option': 'skip', 'anket_id': id})
    like = types.InlineKeyboardButton(text='Лайк', callback_data=like_data)
    skip = types.InlineKeyboardButton(text='Следующий', callback_data=skip_data)
    markup.add(like, skip)
    bot.send_message(message.chat.id, response, reply_markup=markup)
        

@bot.callback_query_handler(func=lambda call: True)
def like_or_skip(callback):
    callback_data = json.loads(callback.data)
    if callback_data['option'] == 'like':
        user = users['user']
        id = callback_data['anket_id']
        code = user.toggle_like(id)
        bot.answer_callback_query(callback.id, text=str(code))
    else:
        bot.answer_callback_query(callback.id, text='You skip this anketa')


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, \nдля начала тебе в обязательном порядке нужно войти в свой аккаунт\n(если ты еще не зарегистрирован, то можешь создать акканут по API: http://127.0.0.1:8000/account/auth/users/ ))')
    bot.send_message(message.chat.id,'Введи свои данные в следующем формате:\nexample_username\nexample_password')
    bot.register_next_step_handler(message,auth_user)

def auth_user(message):
    username,password = message.text.split('\n')
    user = AuthUser(username,password)
    res,is_user_auth = user.authenticate_user()
    bot.send_message(message.chat.id,res)
    if is_user_auth == True:
        users['user'] = user
        bot.send_message(message.chat.id,'Введите что либо чтобы получить первую анкету')
        bot.register_next_step_handler(message,send_ankets)
    if is_user_auth == False:
        bot.register_next_step_handler(message,error)

def send_ankets(message):
    user = users['user']
    ankets = user.get_ankets()
    for x in range(len(ankets)):
        send_next_anket(message,ankets,x)
    bot.send_message(message.chat.id, 'Анкеты закончились')


def error(message):
    bot.send_message(message.chat.id,'Извините но вы не вошли в систему')










bot.polling()