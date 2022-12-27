# Прикрутить бота. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
from config import TOKEN
import math

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_commmand(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hello\n/help\n\nЧто я умею:\n/sum - складывать 2 числа\n\
        /diff - считать разность 2-х чисел\n/mult - умножать 2 числа\n/div - делить первое число на второе\n\
        /pow - возводить в целочисленную степень\n/sqrt - извлекать квадратный корень\nКоманду и числа нужно вводить через пробел')

def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.message.text}\n')
    file.close()

def sum_number(update: Update, context: CallbackContext):     
    log(update, context)
    msg = update.message.text
    if ',' in msg:
        update.message.reply_text('Некорректный ввод разделителя')
    else:
        items = msg.split()
        if not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} + {y} = {x + y}')
        elif items[1].isalpha():
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[1]}')
        else:
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[2]}')

def diff_number(update: Update, context: CallbackContext):
    log(update, context)     
    msg = update.message.text
    if ',' in msg:
        update.message.reply_text('Некорректный ввод разделителя')
    else:
        items = msg.split()
        if not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} - {y} = {x - y}')
        elif items[1].isalpha():
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[1]}')
        else:
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[2]}')

def mult_number(update: Update, context: CallbackContext):
    log(update, context)     
    msg = update.message.text
    if ',' in msg:
        update.message.reply_text('Некорректный ввод разделителя')
    else:
        items = msg.split()
        if not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} * {y} = {x * y}')
        elif items[1].isalpha():
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[1]}')
        else:
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[2]}')

def div_number(update: Update, context: CallbackContext):
    log(update, context)     
    msg = update.message.text
    if ',' in msg:
        update.message.reply_text('Некорректный ввод разделителя')
    else:
        items = msg.split()
        if not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            if not y == 0:
                update.message.reply_text(f'{x} / {y} = {x / y}')
            else:
                update.message.reply_text(f'Деление на {y} невозможно')
        elif items[1].isalpha():
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную {items[1]}')
        elif items[2] == 0:
            update.message.reply_text(f'Делить на {y} нельзя')
        else:
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную {items[2]}')

def pow_number(update: Update, context: CallbackContext):
    log(update, context)     
    msg = update.message.text
    if ',' in msg:
        update.message.reply_text('Некорректный ввод разделителя')
    else:
        items = msg.split()
        if not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            y_int = int(y)
            if y - y_int == 0:
                update.message.reply_text(f'{x} ^ {y} = {x ** y}')
            else:
                update.message.reply_text(f'Значение степени дробное число. Данной программой возведение в дробную степень не предусмотрено')
        elif items[1].isalpha():
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[1]}')
        else:
            update.message.reply_text(f'Некорректный ввод. Одна из переменных не число. Вы ввели переменную --> {items[2]}')

def sqrt_number(update: Update, context: CallbackContext):
    log(update, context)     
    msg = update.message.text
    if ',' in msg:
        update.message.reply_text('Некорректный ввод разделителя')
    else:
        items = msg.split()
        if len(items) < 3 and not items[1].isalpha():
            x = float(items[1])
            update.message.reply_text(f'sqrt {x} = {math.sqrt(x)}')
        elif len(items) >= 3:
            update.message.reply_text(f'Введен лишний аргумент --> {items[2]}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели переменную --> {items[1]}')


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help_commmand))
updater.dispatcher.add_handler(CommandHandler('sum', sum_number))
updater.dispatcher.add_handler(CommandHandler('dff', diff_number))
updater.dispatcher.add_handler(CommandHandler('mult', mult_number))
updater.dispatcher.add_handler(CommandHandler('div', div_number))
updater.dispatcher.add_handler(CommandHandler('pow', pow_number))
updater.dispatcher.add_handler(CommandHandler('sqrt', sqrt_number))

print('сервер запущен')                                      
updater.start_polling()                                 
updater.idle()  