import telebot
from telebot import types
import log_db

types_num = 0

bot = telebot.TeleBot("6060190526:AAHqT7w0aBVIvlmPE_MfrUbbZ0jnmL2xgbE")
#https://t.me/Sem_Sem8bot

@bot.message_handler(commands=["start"])
def calc(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Рациональные')
    key2 = types.KeyboardButton('Комплексные ')
    markup.add(key1, key2)
    bot.send_message(message.chat.id, f'Калькулятор', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def buttons(message):
    global types_num
    a = types.ReplyKeyboardRemove()
    if message.text == 'Рациональные':
        bot.send_message(message.chat.id, f'Выбран режим рациональных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f"Выедите выражение разделяя пробелом")
        bot.register_next_step_handler(message, controller)
        types_num = 0
    elif message.text == 'Комплексные':
        bot.send_message(message.chat.id, f'Выбран режим комплексных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f"Выедите выражение разделяя пробелом")
        bot.register_next_step_handler(message, controller)
        types_num = 1


def controller(message):
    line = message.text.split()
    znak = line[1]
    res = ''
    if types_num == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])

    if znak == "+":
        res = summ_nums(a,b)
    elif znak == '-':
        res = sub_nums(a, b)
    elif znak == '*':
        res = mult_nums(a, b)
    elif znak == '/':
        res = div_nums(a, b)
    elif types_num == 1 and (znak =='//' or znak == '%'):
        bot.send_message(message.chat.id, 'Неверный ввод, try again')
        bot.register_next_step_handler(message, controller)
        return
    elif znak == '//':
        res = div_int(a, b)
    elif znak == '%':
        res = div_rem(a, b)
    log_db.save_data(res, message)
    bot.send_message(message.chat.id, str(res))


def summ_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def mult_nums(a, b):
    return a * b

def div_nums(a, b):
    return a / b

def div_int(a, b):
    return a//b

def div_rem(a, b):
    return a%b

bot.infinity_polling()