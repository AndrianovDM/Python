from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters


bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher

def message(update, context):
    text = update.message.text
    text = text.replace('абв', '')
    context.bot.send_message(update.effective_chat.id, text)

message_handler = MessageHandler(Filters.text, message)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()