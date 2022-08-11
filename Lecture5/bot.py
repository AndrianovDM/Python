from bots_command import *

app = ApplicationBuilder().token("5503501873:AAEKY5M1ZZu_W6sRJqRvXrNyXAEJvmWR_9c").build()
print('server start')
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
