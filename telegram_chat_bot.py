# 6274528723:AAEmccVb_t-0Tc1uS9GVLbSGARmbiCbh9Uw

import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# This loads environment variables from a .env file
load_dotenv()

telegram_token = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Ask me anything.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can ask me any question!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # You can customize the responses or integrate a more complex logic here
    response = 'You said: ' + text
    await update.message.reply_text(response)

def main():
    # Replace 'YOUR_TOKEN' with the token you got from BotFather
    application = Application.builder().token(telegram_token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
