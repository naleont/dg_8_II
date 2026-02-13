# Проект. Telegram-бот. Задание 4. Наполнение бота

Если вы получили замечания к предыдущему заданию, не забудьте их исправить.

## Задание

В вашем файле со "скелетом" бота допишите наполнение всех функций: так, чтобы все они выполняли свои задачи. Не забывайте проверять работоспособность каждого реализованного этапа работы вашего алгоритма.

## Пример готового бота

```python
import telebot
from my_token import TOKEN

bot = telebot.TeleBot(TOKEN)

data = {}

# 2 Учитесь в школе?
def school_student(message):
    markup = telebot.types.InlineKeyboardMarkup()
    item_1 = telebot.types.InlineKeyboardButton(text='Да', callback_data='school_student-yes')
    item_2 = telebot.types.InlineKeyboardButton(text='Нет', callback_data='school_student-no')
    markup.add(item_1, item_2)
    bot.send_message(message.chat.id, 'Вы учитесь в школе?', reply_markup=markup)


# 4 Какой класс?
def school_class(message):
    markup = telebot.types.ForceReply(input_field_placeholder='10', selective=False)
    bot.register_next_step_handler(message, school_class_handler)
    bot.send_message(message.chat.id, 'В каком вы классе?', reply_markup=markup)


# 5 Обработка ответа - какой класс
def school_class_handler(message):
    data['school_class'] = message.text
    good_sleep(message)


# 6 Выспались?
def good_sleep(message):
    markup = telebot.types.InlineKeyboardMarkup()
    item_1 = telebot.types.InlineKeyboardButton(text='Да', callback_data='good_sleep-yes')
    item_2 = telebot.types.InlineKeyboardButton(text='Нет', callback_data='good_sleep-no')
    markup.add(item_1, item_2)
    bot.send_message(message.chat.id, 'Вы сегодня выспались?', reply_markup=markup)


# 1 Начало опроса
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
    'Спасибо, что согласились принять участие в опросе! Он займет всего пару минут. Все данные хранятся анонимно.')
    school_student(message)


# 3 Обработка ответа - учитесь в школе
@bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'school_student')
def school_student_handler(call):
    reply = call.data.split('-')[1]
    data['school_student'] = reply
    if reply == 'yes':
        school_class(call.message)
    else:
        data['school_class'] = ''
        good_sleep(call.message)
        

# 7 Обработка ответа - выспались
@bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'good_sleep')
def good_sleep_handler(call):
    reply = call.data.split('-')[1]
    data['good_sleep'] = reply
    if reply == 'yes':
        # 8 Здорово!
        bot.send_message(call.message.chat.id, 'Здорово!')
    else:
        # 9 Надо выспаться
        bot.send_message(call.message.chat.id, 'Сон - это важно! Не забудьте выспаться сегодня!')
    # 10 Спасибо за участие!
    bot.send_message(call.message.chat.id, 'Опрос завершен, спасибо за участие!')

bot.polling(none_stop=True)
```