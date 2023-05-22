import telebot
from telebot import types

from nedelya import curr_week_for_bd, curr_week
from bd import get_day_formatting, get_week_formatting

token = '6097277425:AAG2CSWJdq4eAdHJAqNtl2wur1V6BcFICE4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("/help", "/mon", "/tue", "/wen", "/thu", "/fri", "/satt","/curr", "/next")
    mess = f'Здравствуйте, <em>{message.from_user.first_name}</em>!\nЯ бот для отображения расписания❤\nНапишите /help, чтобы узнать что я умею'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='Напишите /week - для того, чтобы узнать, какая сейчас неделя\nНапишите /mtuci - для того, чтобы попасть на сайт МТУСИ\nУ меня есть такие команды:\n/mon - расписание на понедельник\n/tue - на вторник \n/wen - на среду \n/thu - на четверг \n/fri - на пятницу \n/satt - на субботу \n/curr - на текущую неделю \n/next - на следующую неделю')


@bot.message_handler(commands=['week'])
def help(message):
    bot.send_message(message.chat.id, text=f'Сейчас {curr_week()} неделя')


@bot.message_handler(commands=['mtuci'])
def help(message):
    bot.send_message(message.chat.id, text='Сайт МТУСИ: https://mtuci.ru')


@bot.message_handler(commands=['mon'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 1))}', parse_mode='HTML')


@bot.message_handler(commands=['tue'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 2))}', parse_mode='HTML')


@bot.message_handler(commands=['wen'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 3))}', parse_mode='HTML')


@bot.message_handler(commands=['thu'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 4))}', parse_mode='HTML')


@bot.message_handler(commands=['fri'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 5))}', parse_mode='HTML')


@bot.message_handler(commands=['satt'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 6))}', parse_mode='HTML')


@bot.message_handler(commands=['curr'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_week_formatting(curr_week_for_bd(1)))}', parse_mode='HTML')


@bot.message_handler(commands=['next'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_week_formatting(curr_week_for_bd(1)))}', parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, text='Я вас не понимаю, обратитесь к команде /help')


bot.polling(none_stop=True, interval=0)
