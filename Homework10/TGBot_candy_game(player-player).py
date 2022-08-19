from tkinter import FIRST
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from random import randint

OPERATION = 0
FIRST_GAMER = 1
NEXT_STEP_ONE = 2
NEXT_STEP_TWO = 3
CANCEL = 4
draw = randint(1, 2)
bot = Bot(token='5447945174:AAG0zVJ2blMBNPStxO9HMk1L5eir0O4N5m4')
updater = Updater(token='5447945174:AAG0zVJ2blMBNPStxO9HMk1L5eir0O4N5m4')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'ДОБРО ПОЖАЛОВАТЬ В ИГРУ С КОНФЕТАМИ!!!\n')
    context.bot.send_message(update.effective_chat.id, 'Введите количество конфет на столе:\n')
    return OPERATION

def operation(update, context):
    global draw
    global count_one
    global count_two
    global total
    count_one = 0
    count_two = 0
    total = int(update.message.text)
    if draw == 1:
        context.bot.send_message(update.effective_chat.id, 'Ходит игрок №1. \n') 
        context.bot.send_message(update.effective_chat.id, f'Игрок №{draw} - введите количество конфет, от 1 до 28: ')      
    else: 
        context.bot.send_message(update.effective_chat.id, 'Ходит игрок №2. \n')
        context.bot.send_message(update.effective_chat.id, f'Игрок №{draw} - введите количество конфет, от 1 до 28: ')  
    return FIRST_GAMER

def first_gamer(update, context):
    global numberOne
    global total
    global count_one
    global draw
    if draw == 1:
        numberOne = int(update.message.text)
        if numberOne < 1 or numberOne > 28:
            context.bot.send_message(update.effective_chat.id, f'Игрок №{draw}, введите корректное количество конфет: ')
            numberOne = int(update.message.text)
        total -= numberOne 
        count_one += numberOne
        context.bot.send_message(update.effective_chat.id, f'Взял {numberOne}, теперь у игрока №{draw}: {count_one}.\n'
                                                                f'На столе осталось {total}.\n')
        draw = 2
        if total < 28:
            context.bot.send_message(update.effective_chat.id,'Победил игрок №1')  
            return cancel(update, context)
        context.bot.send_message(update.effective_chat.id, 'Ходит игрок №2.\n')
        context.bot.send_message(update.effective_chat.id, f'Игрок №2, введите корректное количество конфет: ')

    return NEXT_STEP_TWO

def second_gamer(update, context):
    global numberTwo
    global total
    global count_two
    global draw
    if draw == 2:
        numberTwo = int(update.message.text)
        if numberTwo < 1 or numberTwo > 28:
            context.bot.send_message(update.effective_chat.id, f'Игрок №{draw}, введите корректное количество конфет: ')
            numberTwo = int(update.message.text)
        total -= numberTwo 
        count_two += numberTwo
        context.bot.send_message(update.effective_chat.id, f'Взял {numberTwo}, теперь у игрока №{draw}: {count_two}.\n'
                                                                f'На столе осталось {total}.\n')
        draw = 1
        if total < 28:
            context.bot.send_message(update.effective_chat.id,'Победил игрок №2')
            return cancel(update, context)
        context.bot.send_message(update.effective_chat.id, 'Ходит игрок №1.\n')
        context.bot.send_message(update.effective_chat.id, f'Игрок №1, введите корректное количество конфет: ')
        
        return NEXT_STEP_ONE

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Отличная игра!')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
oper_handler = MessageHandler(Filters.text, operation)
first_gamer_handler = MessageHandler(Filters.text, first_gamer)
second_gamer_handler = MessageHandler(Filters.text, second_gamer)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={
                                            FIRST_GAMER: [first_gamer_handler],
                                            NEXT_STEP_ONE: [first_gamer_handler],
                                            NEXT_STEP_TWO: [second_gamer_handler],
                                            OPERATION: [oper_handler],
                                    },
                                    fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()

# def operation(update, context):

#     draw = randint(1, 2)


#     global count

#     que = update.callback_query
#     var = que.data
#     que.answer()
#     array_base = create_arr(size, '*')
#     context.bot.send_message(update.effective_chat.id, f'{outlet(array_base)}')    
#     if st == 1:
#         context.bot.send_message(update.effective_chat.id, 'Ходит О:')
#     else:
#         context.bot.send_message(update.effective_chat.id, 'Ходит X:')
#     return FIRST_GAMER
