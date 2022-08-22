# Copy copy_packname to packname

import telebot
import json
from PIL import Image
import os

USERID = "1686862883"
bot = telebot.TeleBot(token="1942776248:AAFlJ1Nvc4NNhnlSKXafZQEvMgayR-4n7VE")
name = 'loveGenshin'
packname = name +'_by_hyoling_bot'
copy_packname = "hyoyuseopjin"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Start Test!')

@bot.message_handler(commands=['addsticker'])
def start(message):
    sent = bot.send_message(message.chat.id, "Send packname to copy")
    bot.register_next_step_handler(sent, copy_pack)

def copy_pack(message):
    copy_packname = message.text
    copyset = bot.get_sticker_set(copy_packname)
    for i in range(len(copyset.stickers)):
        sticker = copyset.stickers[i]
        sticker_file_info = bot.get_file(sticker.file_id)
        new_sticker_file = bot.download_file(sticker_file_info.file_path)

        with open("sticker.webp", 'wb') as new_file:
            new_file.write(new_sticker_file)
        imgbp = Image.open("sticker.webp")
        imgbp.save("sticker.png", "png")
        os.remove("sticker.webp")
        fID = bot.upload_sticker_file(USERID, open("sticker.png", "rb")).file_id
        print("success upload!")

        try:
            bot.get_sticker_set(packname)
            bot.add_sticker_to_set(
                message.chat.id,
                name=packname,
                png_sticker=fID,
                emojis=sticker.emoji
            )
            bot.send_message(message.chat.id, "%d Sticker has been added successfully"%i)
        except:
            bot.create_new_sticker_set(message.chat.id, packname, name,sticker.emoji,open("sticker.png", "rb"))
            bot.send_message(message.chat.id, "Sticker pack has been added successfully")
    

if __name__ == '__main__':
    # start_message(message)
    bot.infinity_polling()