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
                if message.text.lower() == 'привет':
                    bot.send_message(call.message.chat.id, "Привет! Расскажите что-нибудь веселенькое или анекдот:))")
                elif message.text.lower() == 'как настроение?':
                    bot.send_message(call.message.chat.id, "У меня отличное настроение. А у вас?")
                elif message.text.lower() == 'доброе утро':
                    bot.send_message(call.message.chat.id, "Доброе утро")
                elif message.text.lower() == 'добрый день':
                    bot.send_message(call.message.chat.id, "Добрый день")
                elif message.text.lower() == 'привет!':
                    bot.send_message(call.message.chat.id, "Привет! Расскажите что-нибудь веселенькое или анекдот:))")
                elif message.text.lower() == 'сколько тебе лет?':
                    bot.send_message(call.message.chat.id, "Вопрос некорректный и скорее бесполезный. Я робот(программа) Меня запустили на сервере 6 Сентября 2020 года. \nЯ не старею, а только совершенствуюсь. И работаю пока люди во мне нуждаются")
                elif message.text.lower() == 'прости, если обидел':
                    bot.send_message(call.message.chat.id, "Да ну, что вы. Я не обижаюсь. \nРоботы не умеют обижаться и программы тоже)). \nРасскажи что-нибудь веселенькое. Посмеемся вместе-:)")
                elif message.text.lower() == 'веселое':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'мне весело)':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'нормальное':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'норма!':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'норма':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'хорошее':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'супер':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'супер!':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'супер!!!':
                    bot.send_message(call.message.chat.id, "Вот и отлично:) Давайте общаться.")
                elif message.text.lower() == 'спасибо':
                    bot.send_message(call.message.chat.id, "Рад вас развеселить:-)")
                elif message.text.lower() == 'благодарю':
                    bot.send_message(call.message.chat.id, "Не стоит благодарностей. Всегда к вашим услугам-)")
                elif message.text.lower() == 'грустное':
                    bot.send_message(call.message.chat.id, "Я вас развеселю -^--^-, просто нажми Давай пошутим-^--^-", reply_markup = keyboard2)
                elif message.text.lower() == 'грустное(':
                    bot.send_message(call.message.chat.id, "Я вас развеселю -^--^-, просто нажми Давай пошутим-^--^-", reply_markup=keyboard2)
                elif message.text.lower() == 'мне грустно(':
                    bot.send_message(call.message.chat.id, "Я вас развеселю -^--^-, просто нажми Давай пошутим-^--^-", reply_markup=keyboard2)
                elif message.text.lower() == 'как погода?':
                    bot.send_message(call.message.chat.id, "Пасмурно или солнечно, холодно или жарко. Чтобы это понять выгляните в окно или спросите у яндекса или гугла. https://yandex.ru/pogoda/213")
                elif message.text.lower() == 'пока':
                    bot.send_message(call.message.chat.id, "Уже уходишь? ну тогда пока.")
                elif message.text.lower() == 'как дела?':
                    bot.send_message(call.message.chat.id, "Отлично! А у тебя?")
                elif message.text.lower() == 'тоже отлично':
                    bot.send_message(call.message.chat.id, "Ну отлично! тогда повеселимся.")
                elif message.text.lower() == 'добрый вечер':
                    bot.send_message(call.message.chat.id, "Добрый вечер")
                elif message.text.lower() == 'спокойной ночи':
                    bot.send_message(call.message.chat.id, "Спокойной ночи!")
                else:
                    bot.send_message(call.message.chat.id, "С вами так весело)):):):)", reply_markup = keyboard2)

bot.polling()
