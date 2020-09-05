# -*- coding: utf8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot('1197373164:AAGqGxhxWdqVxbixaz9bR2oqhW3-gJdwQqY')


@bot.message_handler(commands=['start'])
def start_messages(message):
    keyboard1 = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Давай пошутим", callback_data='Давай пошутим')
    callback_button2 = types.InlineKeyboardButton(text="Давай поболтаем", callback_data='Давай поболтаем')
    keyboard1.add(callback_button1, callback_button2)
    bot.send_message(message.chat.id, "Привет! Я робот - шутник, Меня зовут Алексейсич, люблю шутить и смеяться. Чтобы начать шутить нажмите Давай пошутим, \nЕсли хотите поговорить со мной, то нажмите Давай поболтаем после этого начните вводить сообщения.", reply_markup = keyboard1)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard2 = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Давай пошутим", callback_data='Давай пошутим')
    callback_button2 = types.InlineKeyboardButton(text="Давай поболтаем", callback_data='Давай поболтаем')
    keyboard2.add(callback_button1, callback_button2)
    keyboard3 = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="1", callback_data='1')
    callback_button2 = types.InlineKeyboardButton(text="2", callback_data='2')
    callback_button3 = types.InlineKeyboardButton(text="3", callback_data='3')
    callback_button4 = types.InlineKeyboardButton(text="4", callback_data='4')
    callback_button5 = types.InlineKeyboardButton(text="5", callback_data='5')
    callback_button6 = types.InlineKeyboardButton(text="чат", callback_data='Давай поболтаем')
    keyboard3.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
    if call.message:
        if call.data == "Давай пошутим":
            bot.send_message(call.message.chat.id, "Чтобы прочитать шутки нажмите кнопки 1...5. Чтобы пообщаться с мной(ботом) нажмите чат", reply_markup = keyboard3)
        elif call.data == "1":
            bot.send_message(call.message.chat.id,
                                 "Это правда, что ты можешь купить Волгу? \n- Да. Но зачем мне столько воды? \nДля продолжения нажмите любую цифру или чат чтобы поговорить со мной(ботом)", reply_markup = keyboard3)
        elif call.data == "2":
            bot.send_message(call.message.chat.id,
                                 "В школе на уроке географии:\n- Дети, далеко ли от нас находится Китай? - спрашивает учительница.\n- Не далеко! "
                                 "- отвечает Вовочка. \n- Почему ты так думаешь? \n-А к нашей соседке частенько заходит китаец, "
                                 "так он к ней на велосипеде приезжает.\nДля продолжения нажмите любую цифру или чат чтобы поговорить со мной(ботом)", reply_markup = keyboard3)
        elif call.data == "3":
            bot.send_message(call.message.chat.id, "- Медведи! Медведи! - испуганно кричали убегающие туристы."
                                                  "\n- Туристы! Туристы! - радостно рычали догоняющие мишки. Нажмите любую цифру или чат чтобы поговорить со мной(ботом)", reply_markup = keyboard3)
        elif call.data == "4":
            bot.send_message(call.message.chat.id, "— Ужасный ресторан! У вас устриц нет, тефтелей нет! \nПринесите моё пальто!\n— К сожалению, вашего пальто тоже нет, Нажмите любую цифру или чат чтобы поговорить со мной(ботом)", reply_markup = keyboard3)
        elif call.data == "5":
            bot.send_message(call.message.chat.id, "В детстве я ждал когда прогреется кинескоп, сейчас я жду, когда у телевизора загрузится операционка. В чем прогресс? Нажмите любую цифру или чат чтобы поговорить со мной(ботом)", reply_markup = keyboard3)
        elif call.data == "Давай поболтаем":
            @bot.message_handler(content_types=["text"])
            def text_messages(message):
                if message.text == 'Привет':
                    bot.send_message(call.message.chat.id, "Привет!")
                elif message.text == 'Как настроение?':
                    bot.send_message(call.message.chat.id, "У меня отличное настроение. А у вас?")
                elif message.text == 'грустное':
                    bot.send_message(call.message.chat.id, "Я вас развеселю -^--^-, просто нажми Давай пошутим-^--^-", reply_markup = keyboard2)
                elif message.text == 'Как погода?':
                    bot.send_message(call.message.chat.id, "Пасмурно или солнечно, холодно или жарко. Чтобы это понять выгляните в окно или спросите у яндекса или гугла. https://yandex.ru/pogoda/213")
                else:
                    bot.send_message(call.message.chat.id, "С вами так весело)):):):)", reply_markup = keyboard2)

bot.polling()