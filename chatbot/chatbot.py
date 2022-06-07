import random
import configArray
import telebot
from telebot import types

bot = telebot.TeleBot('5480883581:AAGMc7-ODFXsChVImC6JUM4Pn6WkgJ18n0M')


@bot.message_handler(commands=['start'])
def welcome(message):

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # наша клавиатура
    key_movie = types.KeyboardButton("Фильм")  # кнопка фильм
    key_series = types.KeyboardButton("Сериал")  # кнопка сериал
    markup.add(key_movie, key_series)  # добавляем кнопки

    # Приветствие
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>. \nЕсли у вас нет друга-киномана или он есть, но прочитал сообщение и не ответил, то взгляните на телеграм-бота, который порекомендует годный фильм по вашим предпочтениям.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    question = 'Что хотите посмотреть?'
    bot.send_message(message.from_user.id, text=question)


@bot.message_handler(content_types=['text'])
def choice(message):
    if message.text == 'Фильм':  # Вывод жанров

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        item1 = types.KeyboardButton("Буду смотреть со своей второй половинкой 💗")
        item2 = types.KeyboardButton("Точно позову пару друзей 🥳")
        item3 = types.KeyboardButton("Буду смотреть фильм в одиночестве… Только я и мой попкорн 😂")
        item4 = types.KeyboardButton("Пока не знаю 🙄")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Есть ли у тебя компания на вечер?', reply_markup=markup)
        bot.register_next_step_handler(message, question1_film)

    elif message.text == 'Сериал':  # Вывод сериалов

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        item11 = types.KeyboardButton("Поплакать 🙄")
        item22 = types.KeyboardButton("Вдохновиться 🥳")
        item33 = types.KeyboardButton("Испугаться 😂")
        item44 = types.KeyboardButton("Посмеяться 😂")

        markup1.add(item11, item22, item33, item44)
        bot.send_message(message.chat.id, 'Чего больше хочется?', reply_markup=markup1)
        bot.register_next_step_handler(message, question1_serial)

    elif message.text == 'Пройти тест заново':
        # Клавиатура
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # клавиатура
        key_movie = types.KeyboardButton("Фильм")  # кнопка фильм
        key_series = types.KeyboardButton("Сериал")  # кнопка сериал
        markup.add(key_movie, key_series)  # добавляем кнопки

        # Приветствие
        bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, тестовый бот.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)
        question = 'Что хочешь посмотреть?'
        bot.send_message(message.from_user.id, text=question)


# для фильма
def question1_film(message):
    if message.text == 'Буду смотреть со своей второй половинкой 💗':
        configArray.arrayResult[0] += 1
        answer1_film(message)
    elif message.text == 'Точно позову пару друзей 🥳':
        configArray.arrayResult[0] += 1
        answer1_film(message)
    elif message.text == 'Буду смотреть фильм в одиночестве… Только я и мой попкорн 😂':
        configArray.arrayResult[0] += 1
        answer1_film(message)
    elif message.text == 'Пока не знаю 🙄"':
        configArray.arrayResult[0] += 1
        answer1_film(message)


def question2_film(message):
    if message.text == 'Закажу что-то и устрою романтический вечер 😍':
        configArray.arrayResult[0] += 1
        answer2_film(message)
    elif message.text == 'Попкорн и чипсы — это нестареющая классика!':
        configArray.arrayResult[0] += 1
        answer2_film(message)
    elif message.text == 'Принесу все вкусненькое, что есть в холодильнике 😋':
        configArray.arrayResult[0] += 1
        answer2_film(message)
    elif message.text == 'Приготовлю что-то необычное 😉':
        configArray.arrayResult[0] += 1
        answer2_film(message)


def question3_film(message):
    if message.text == 'Драма 💔':
        configArray.arrayResult[0] += 1
        answer3_film(message)
    elif message.text == 'Комедия 😃':
        configArray.arrayResult[0] += 1
        answer3_film(message)
    elif message.text == 'Фантастика ✨':
        configArray.arrayResult[0] += 1
        answer3_film(message)
    elif message.text == 'Ужасы 👻':
        configArray.arrayResult[0] += 1
        answer3_film(message)


def question4_film(message):
    if message.text == 'Смотрю трейлеры на YouTube':
        configArray.arrayResult[0] += 1
        answer4_film(message)
    elif message.text == 'Спрашиваю у друзей.':
        configArray.arrayResult[0] += 1
        answer4_film(message)
    elif message.text == 'Просто захожу на сайт и подбираю по параметрам.':
        configArray.arrayResult[0] += 1
        answer4_film(message)
    elif message.text == 'Читаю отзывы и рецензии.':
        configArray.arrayResult[0] += 1
        answer4_film(message)


def question5_film(message):
    if message.text == 'Мечтательное и романтичное 😍':
        configArray.arrayResult[0] += 1
        film(message)
    elif message.text == 'Хочется отключить голову, нужен отдых 😔':
        configArray.arrayResult[0] += 1
        film(message)
    elif message.text == 'Настроение в норме, как и всегда 😉':
        configArray.arrayResult[0] += 1
        film(message)
    elif message.text == 'Могло бы быть и лучше 😢':
        configArray.arrayResult[0] += 1
        film(message)


# для сериала
def question1_serial(message):
    if message.text == 'Поплакать 🙄':
        configArray.arrayResult[0] += 1
        answer1_serial(message)
    elif message.text == 'Вдохновиться 🥳':
        configArray.arrayResult[0] += 1
        answer1_serial(message)
    elif message.text == 'Испугаться 😂':
        configArray.arrayResult[0] += 1
        answer1_serial(message)
    elif message.text == 'Посмеяться 😂':
        configArray.arrayResult[0] += 1
        answer1_serial(message)


def question2_serial(message):
    if message.text == 'Когда как.':
        configArray.arrayResult[0] += 1
        answer2_serial(message)
    elif message.text == 'Люблю, когда кто-то работает за меня 😂':
        configArray.arrayResult[0] += 1
        answer2_serial(message)
    elif message.text == 'Нет, не очень.':
        configArray.arrayResult[0] += 1
        answer2_serial(message)
    elif message.text == 'Да.':
        configArray.arrayResult[0] += 1
        answer2_serial(message)


def question3_serial(message):
    if message.text == 'Сериал «Элита».':
        configArray.arrayResult[0] += 1
        answer3_serial(message)
    elif message.text == 'Какой-нибудь мультсериал… Например, «Рик и Морти».':
        configArray.arrayResult[0] += 1
        answer3_serial(message)
    elif message.text == 'Сериал «Доктор Кто».':
        configArray.arrayResult[0] += 1
        answer3_serial(message)
    elif message.text == 'Сериал «Леденящие душу приключения Сабрины».':
        configArray.arrayResult[0] += 1
        answer3_serial(message)


def question4_serial(message):
    if message.text == 'Затронуть чувства 💔':
        configArray.arrayResult[0] += 1
        answer4_serial(message)
    elif message.text == 'Поднять настроение 😄':
        configArray.arrayResult[0] += 1
        answer4_serial(message)
    elif message.text == 'Заставить задуматься о чем-то важном 🤔':
        configArray.arrayResult[0] += 1
        answer4_serial(message)
    elif message.text == 'Вызвать у меня желание посмотреть его еще раз 😉':
        configArray.arrayResult[0] += 1
        answer4_serial(message)


def question5_serial(message):
    if message.text == 'В кровати 😴':
        configArray.arrayResult[0] += 1
        serial(message)
    elif message.text == 'В гостиной, на удобном диванчике 😊':
        configArray.arrayResult[0] += 1
        serial(message)
    elif message.text == 'На кухне, поближе к еде 😂':
        configArray.arrayResult[0] += 1
        serial(message)
    elif message.text == 'В любом месте, где можно поставить ноутбук 💻':
        configArray.arrayResult[0] += 1
        serial(message)


def film(message):

    if configArray.arrayResult.index(max(configArray.arrayResult)) == 0:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_comedy))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 1:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_crime))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 2:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_drama))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 3:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_action))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 4:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_fantastic))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 5:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_fantasy))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 6:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.film_horror))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item1 = types.KeyboardButton("Пройти тест заново")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup)


def serial(message):
    if configArray.arrayResult.index(max(configArray.arrayResult)) == 0:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_comedy))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 1:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_crime))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 2:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_drama))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 3:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_action))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 4:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_fantastic))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 5:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_fantasy))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)

    elif configArray.arrayResult.index(max(configArray.arrayResult)) == 6:
        clear_data()
        bot.send_message(message.chat.id, text='Советуем посмотреть:')
        bot.send_message(message.chat.id, random.choice(configArray.serial_horror))

        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Добавляем кнопку "Пройти тест заново"
        item11 = types.KeyboardButton("Пройти тест заново")
        markup1.add(item11)
        bot.send_message(message.chat.id, 'Желаете пройти тест заново?', reply_markup=markup1)


def answer1_film(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Закажу что-то и устрою романтический вечер 😍")
    item2 = types.KeyboardButton("Попкорн и чипсы — это нестареющая классика!")
    item3 = types.KeyboardButton("Принесу все вкусненькое, что есть в холодильнике 😋")
    item4 = types.KeyboardButton("Приготовлю что-то необычное 😉")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Какую закуску предпочитаешь под фильм?', reply_markup=markup)
    bot.register_next_step_handler(message, question2_film)


def answer2_film(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Драма 💔")
    item2 = types.KeyboardButton("Комедия 😃")
    item3 = types.KeyboardButton("Фантастика ✨")
    item4 = types.KeyboardButton("Ужасы 👻")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Какой жанр фильма тебе ближе?', reply_markup=markup)
    bot.register_next_step_handler(message, question3_film)


def answer3_film(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Смотрю трейлеры на YouTube")
    item2 = types.KeyboardButton("Спрашиваю у друзей.")
    item3 = types.KeyboardButton("Просто захожу на сайт и подбираю по параметрам.")
    item4 = types.KeyboardButton("Читаю отзывы и рецензии.")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Как ты обычно выбираешь фильм?', reply_markup=markup)
    bot.register_next_step_handler(message, question4_film)


def answer4_film(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Мечтательное и романтичное 😍")
    item2 = types.KeyboardButton("Хочется отключить голову, нужен отдых 😔")
    item3 = types.KeyboardButton("Настроение в норме, как и всегда 😉")
    item4 = types.KeyboardButton("Могло бы быть и лучше 😢")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Какое настроение у тебя сегодня?', reply_markup=markup)
    bot.register_next_step_handler(message, question5_film)


# ответы для сериала
def answer1_serial(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Когда как.")
    item2 = types.KeyboardButton("Люблю, когда кто-то работает за меня 😂")
    item3 = types.KeyboardButton("Нет, не очень.")
    item4 = types.KeyboardButton("Да.")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Ты много учишься и работаешь?', reply_markup=markup)
    bot.register_next_step_handler(message, question2_serial)


def answer2_serial(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Сериал «Элита».")
    item2 = types.KeyboardButton("Какой-нибудь мультсериал… Например, «Рик и Морти».")
    item3 = types.KeyboardButton("Сериал «Доктор Кто».")
    item4 = types.KeyboardButton("Сериал «Леденящие душу приключения Сабрины».")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Если бы ты решил(а) посмотреть сериал, то это был бы…', reply_markup=markup)
    bot.register_next_step_handler(message, question3_serial)


def answer3_serial(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("Затронуть чувства 💔")
    item2 = types.KeyboardButton("Поднять настроение 😄")
    item3 = types.KeyboardButton("Заставить задуматься о чем-то важном 🤔")
    item4 = types.KeyboardButton("Вызвать у меня желание посмотреть его еще раз 😉")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Хороший фильм должен…', reply_markup=markup)
    bot.register_next_step_handler(message, question4_serial)


def answer4_serial(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    item1 = types.KeyboardButton("В кровати 😴")
    item2 = types.KeyboardButton("В гостиной, на удобном диванчике 😊")
    item3 = types.KeyboardButton("На кухне, поближе к еде 😂")
    item4 = types.KeyboardButton("В любом месте, где можно поставить ноутбук 💻")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Где ты обычно смотришь сериалы?', reply_markup=markup)
    bot.register_next_step_handler(message, question5_serial)


def clear_data():
    configArray.arrayResult[0] = 0
    configArray.arrayResult[1] = 0
    configArray.arrayResult[2] = 0
    configArray.arrayResult[3] = 0
    configArray.arrayResult[4] = 0
    configArray.arrayResult[5] = 0
    configArray.arrayResult[6] = 0


bot.polling(none_stop=True)