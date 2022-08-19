from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from random import randint

def create_arr(size, sign):
    arr = [[ str(i) for i in range(size+1)]]
    for i in range(size): 
        arr_1 = []
        arr.append(arr_1) 
        for j in range(size+1):
            if j == 0:
                arr_1.append(str(i+1))
            else:
                if sign == '*':
                    arr_1.append('*')
                if sign == 'O':
                    arr_1.append('O')
                if sign == 'X':
                    arr_1.append('X')
    return arr

def outlet(arr):
    return '\n'.join(['               '.join(i) for i in arr])
            
def check(arr, size):
    array_o = create_arr(size, 'O')
    array_trans_o = [[j[i] for j in array_o] for i in range(len(array_o[0]))]
    arr_trans_o = [[j[i] for j in arr] for i in range(len(arr[0]))]
    array_diag_o = []

    array_x = create_arr(size, 'X')
    array_trans_x = [[j[i] for j in array_x] for i in range(len(array_x[0]))]
    array_diag_x = []

    arr_diag_left = [] 
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            if i == j:
                array_diag_o.append(array_o[i][j])
                array_diag_x.append(array_x[i][j])
                arr_diag_left.append(arr[i][j])

    arr_diag_right = []
    for i in range(1,len(arr)):
        arr_diag_right.append(arr[i][-i])

    for i in range(1,len(arr)):
        if arr[i] == array_o[i]:
            return 0

    for i in range(1,len(arr)):
        if arr[i] == array_x[i]:
            return 1

    for i in range(1,len(arr)):
        if arr_trans_o[i] == array_trans_o[i]:
            return 0

    for i in range(1,len(arr)):
        if arr_trans_o[i] == array_trans_x[i]:
            return 1
    
    if array_diag_o == arr_diag_left:
        return 0

    if array_diag_x == arr_diag_left:
        return 1

    if array_diag_o == arr_diag_right:
        return 0

    if array_diag_x == arr_diag_right:
        return 1

def number(number):
    i,j = map(int,input().split())

OPERATION = 0
FIRST_GAMER = 1
NEXT_STEP_ONE = 2
NEXT_STEP_ONE_x = 3
NEXT_STEP_TWO = 4
NEXT_STEP_TWO_o = 5
CANCEL = 6
st = randint(1,2)
bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'ДОБРО ПОЖАЛОВАТЬ В ИГРУ КРЕСТИКИ НОЛИКИ\n'
                                                       'Введите кем хотите играть (O, X): ')
    board = [[InlineKeyboardButton('O', callback_data='0'), InlineKeyboardButton('X', callback_data='1')]]
    update.message.reply_text('Выбери:', reply_markup=InlineKeyboardMarkup(board))
    return OPERATION

def operation(update, context):
    global size 
    global array_base
    global count
    global st
    size = 3
    count = size**2 
    que = update.callback_query
    var = que.data
    que.answer()
    array_base = create_arr(size, '*')
    context.bot.send_message(update.effective_chat.id, f'{outlet(array_base)}')    
    if st == 1:
        context.bot.send_message(update.effective_chat.id, 'Ходит О:')
    else:
        context.bot.send_message(update.effective_chat.id, 'Ходит X:')
    return FIRST_GAMER

def first_gamer(update, context):
    global numberOne
    numberOne = update.message.text
    i,j = map(int,numberOne.split())
    array_base[i][j] = 'O'
    
    if check(array_base,size) == 0: 
        context.bot.send_message(update.effective_chat.id, 'Победил O!!!')
        context.bot.send_message(update.effective_chat.id, outlet(array_base))
        return ConversationHandler.END
    if check(array_base,size) == 1: 
        context.bot.send_message(update.effective_chat.id, 'Победил X!!!')
        context.bot.send_message(update.effective_chat.id, outlet(array_base)) 
        return ConversationHandler.END
    context.bot.send_message(update.effective_chat.id, outlet(array_base))
    context.bot.send_message(update.effective_chat.id, '/x')
    return NEXT_STEP_TWO

def second_gamer(update, context):
    global numberTwo
    numberTwo = update.message.text
    i,j = map(int,numberTwo.split())
    array_base[i][j] = 'X'
    if check(array_base,size) == 0: 
        context.bot.send_message(update.effective_chat.id, 'Победил O!!!')
        context.bot.send_message(update.effective_chat.id, outlet(array_base))
        return ConversationHandler.END
    if check(array_base,size) == 1: 
        context.bot.send_message(update.effective_chat.id, 'Победил X!!!') 
        context.bot.send_message(update.effective_chat.id, outlet(array_base))
        return ConversationHandler.END
    context.bot.send_message(update.effective_chat.id, outlet(array_base))
    context.bot.send_message(update.effective_chat.id, '/o')
    return NEXT_STEP_ONE

def X(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите ячейку по вертикали и горизонтали X: ')
    
def O(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите ячейку по вертикали и горизонтали O: ')

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Отличная игра!')
    return ConversationHandler.END


if st == 1:
    start_handler = CommandHandler('start', start)
    oper_handler = CallbackQueryHandler(operation)
    O_step = CommandHandler('o', O)
    first_gamer_handler = MessageHandler(Filters.text, first_gamer)
    X_step = CommandHandler('x', X)
    second_gamer_handler = MessageHandler(Filters.text, second_gamer)
    cancel_handler = CommandHandler('cancel', cancel)
    conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={
                                            FIRST_GAMER: [first_gamer_handler],
                                            NEXT_STEP_ONE: [O_step,first_gamer_handler],
                                            NEXT_STEP_TWO: [X_step, second_gamer_handler],
                                            OPERATION: [oper_handler],
                                    },
                                    fallbacks=[cancel_handler])
else:
    start_handler = CommandHandler('start', start)
    oper_handler = CallbackQueryHandler(operation)
    O_step = CommandHandler('о', X)
    first_gamer_handler = MessageHandler(Filters.text, second_gamer)
    X_step = CommandHandler('х', O)
    second_gamer_handler = MessageHandler(Filters.text, first_gamer)
    cancel_handler = CommandHandler('cancel', cancel)
    conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={
                                            FIRST_GAMER: [first_gamer_handler],
                                            NEXT_STEP_ONE: [X_step,second_gamer_handler],
                                            NEXT_STEP_TWO: [O_step,first_gamer_handler],
                                            OPERATION: [oper_handler],
                                    },
                                    fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()