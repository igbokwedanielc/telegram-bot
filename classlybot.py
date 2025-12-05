from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging

logging.basicConfig(level=logging.INFO)

# Replace with your bot token
TOKEN = "8557354376:AAHfNEW2CnQRfZ9u3zDKzI1M4n-p2eKflTQ"

async def start(update, context):
    await update.message.reply_text("Hello! The bot is now active 😊")

async def reply(update, context):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    app.run_polling()

if __name__ == "__main__":
    main()
