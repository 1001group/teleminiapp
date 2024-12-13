from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ganti dengan Token bot Anda
TOKEN = '7590187559:AAG3LzMwLj-koPQ_t6Z3IhxpgT0ud0bRMwM'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("Visit Our Mini App", url="https://github.com/1001group/teleminiapp/index.html")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"Hello {user.first_name}, welcome to our Telegram bot!\n"
                              "Click below to start using our service:", reply_markup=reply_markup)

def main():
    # Membuat bot dan updater
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah start
    dispatcher.add_handler(CommandHandler("start", start))

    # Menjalankan bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
