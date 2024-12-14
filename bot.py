from telegram import Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Token bot Anda yang didapat dari BotFather
TOKEN = '7590187559:AAG3LzMwLj-koPQ_t6Z3IhxpgT0ud0bRMwM'

# Fungsi untuk menangani perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Gambadirr yang ingin dikirim
    image_url = 'https://thousimg.site/1001slot/sticker-telegram.webp'  # Ganti dengan URL gambar Anda
    
    # Pesan yang ingin dikirim
    welcome_message = (
        "*1001SLOT AKSES APLIKASI MINI TELEGRAM*🥳\n\n" 
        "Halo bosku🙏 Rasakan Pengalaman Bermain Slot Gacor Online dengan Praktis & tanpa browser lebih aman 🏍💥\n\n"
    )
    # Membuat tombol dengan link
    keyboard = [
        [InlineKeyboardButton("GAME GACOR HARI INI🔥", url="https://t.ly/1001slotutama")],
        [InlineKeyboardButton("SERVER THAILAND🔥", url="https://t.ly/1001slotutama")],
        [InlineKeyboardButton("SERVER KAMBOJA🔥", url="https://t.ly/1001slotutama")],
        [InlineKeyboardButton("SERVER SINGAPORE🔥", url="https://t.ly/1001slotutama")],
        [InlineKeyboardButton("Whatsapp Admin🤝", url="https://wa.me/6282121174261")],
        [InlineKeyboardButton("LINK ALTERNATIF 💥", url="https://t.ly/1001slotutama")]  # Ganti dengan URL yang sesuai
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    

    # Mengirim gambar dengan pesan dan tombol link
    await update.message.reply_photo(
        photo=image_url,
        caption=welcome_message,
        reply_markup=reply_markup,
        parse_mode='MarkdownV2'
    )

# Fungsi utama untuk menjalankan bot
def main() -> None:
    # Membuat aplikasi dengan token
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    # Memulai polling untuk bot
    application.run_polling()

if __name__ == '__main__':
    main()
