import telebot
import json
from PIL import Image
import os
import time

USERID = "1686862883"
bot = telebot.TeleBot(token="1942776248:AAFlJ1Nvc4NNhnlSKXafZQEvMgayR-4n7VE")
name = 'loveRail'
packname = name + '_by_hyoling_bot'
path = "./parse/result"

sticker_emoji = ['😄']


@bot.message_handler(commands=['start'])
def start_message(message):
    sent = bot.send_message(message.chat.id, 'test start')
    print(message.chat.id)
    bot.register_next_step_handler(sent, auto_adder)


def auto_adder(message):
    for filename in os.listdir(path):
        img = os.path.join(path, filename)
        fID = bot.upload_sticker_file(USERID, open(img, "rb")).file_id
        print("photo upload")

        try:
            bot.add_sticker_to_set(
                message.chat.id,
                name=packname,
                png_sticker=fID,
                emojis=sticker_emoji
            )
        except:
            bot.create_new_sticker_set(user_id=message.chat.id, name=packname,
                                       title=name, png_sticker=open(img, "rb"), emojis=sticker_emoji)
            bot.send_message(
                message.chat.id, "Sticker pack has been added successfully")

    bot.send_message(message.chat.id, "Sticker has been added successfully")


if __name__ == '__main__':
    # start_message(message)
    bot.infinity_polling()
