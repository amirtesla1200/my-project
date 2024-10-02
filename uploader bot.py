import random
import telebot
import string

TOKEN = 'your bot token'
bot = telebot.TeleBot(TOKEN)

def generate_unique_code(length=15):

    characters = string.ascii_letters + string.digits
    unique_code = ''.join(random.choice(characters) for _ in range(length))
    return unique_code


code = generate_unique_code()

@bot.message_handler(commands=['start'])
def handle_start(message):

    if message.chat.id == 6061226543:
        @bot.message_handler(content_types=['photo'])
        def handle_photo(message):
            photo_file_id = message.photo[-1].file_id
            file_info = bot.get_file(photo_file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            media_code = f"cuck{code}.jpg"
            with open(media_code ,'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, f"https://t.me/your?start={code}")
    elif len(message.text.split()) > 1:
        parameter = message.text.split()[1]

        photo_path = f"C:/Users/SibeGilan/Desktop/channel bot/cuck{parameter}.jpg"
        try:
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        except Exception as e:
            print(e)
    else:
        bot.reply_to(message, "سلام! خوش آمدید به بات من.")





bot.polling()

