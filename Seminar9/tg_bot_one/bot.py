from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


bot = Bot(token='5447945174:AAG0zVJ2blMBNPStxO9HMk1L5eir0O4N5m4')
updater = Updater(token='5447945174:AAG0zVJ2blMBNPStxO9HMk1L5eir0O4N5m4')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Hello!')


def message(update, context):
    text = update.message.text
    print(text)
    context.bot.send_message(update.effective_chat.id, "Как же вы мне надоели!")


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# В конце |||
updater.start_polling()
updater.idle() # ctrl + C

