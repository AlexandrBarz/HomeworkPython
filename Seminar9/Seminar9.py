from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
from telegram import Update
from anecAPI import anecAPI
from config import TOKEN

def get_joke(update: Update, context: CallbackContext):      # функция, которая возвращает шутку
    after_command = context.args                             # ловим то, что будет после команды с помощью context в виде списка из строк
    print(after_command)                                     # для вывода в терминал (context то, что доступно во всем чате)
    update.message.reply_text(anecAPI.modern_joke())         # для вывода в Телеграмм (update то, что доступно в последнем сообщении). Указываем как ответить, а в (что ответить)


def get_message(update: Update, context: CallbackContext):   # функция, которая отлавливает сообщения
    message = update.message.text                            # ловим последнее сообщение
    print(message)
    if 'прив' in message: 
        update.message.reply_text(f'Взаимно Приветствую!') 
        return None                                           # зацикливание, выход из функции
    update.message.reply_text(f'вы ввели: {message}')    


updater = Updater(TOKEN)                                      # создаем переменную 
dispetcher = updater.dispatcher                               # для связи use диспетчер

joke_handler = CommandHandler('joke', get_joke)               # создаем переменную, которая приравнена к команде для отлавливание шутки. Указываем функцию без скобок, чтобы не вызывалась сразу, а только на команду
message_handler = MessageHandler(Filters.text, get_message)   # ловит сообщения в Телеграмме

dispetcher.add_handler(joke_handler)                          # для связи updater и CommandHandler
dispetcher.add_handler(message_handler)                       # для связи updater и MessageHandler. ДОЛЖНА СТОЯТЬ ПОСЛЕ КОМАНДЫ. ЕСЛИ ПОСТАВИТЬ ТО КОМАНДЫ, ТО ОБРАБОТЧИК КОМАНД РАБОТАТЬ НЕ БУДЕТ


print('сервер запущен')                                       # для того, чтобы понять что все работает
updater.start_polling()                                       # обновляет чат Телеграмма
updater.idle()                                                # остановка сервера. Остановка Ctrl+C обрабатывает данная функция idle