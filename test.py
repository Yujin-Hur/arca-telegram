import telebot
import json
from PIL import Image
import os
import time

USERID = "1686862883"
bot = telebot.TeleBot(token="1942776248:AAFlJ1Nvc4NNhnlSKXafZQEvMgayR-4n7VE")
name = 'loveGenshin'
packname = name +'_by_hyoling_bot'
 
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'test start')
    
def get_stickerid(message):

    # JSON DICTIONARY
    all_stick_data = {"file_id": message.sticker.file_id, "width": message.sticker.width,
              "height": message.sticker.height,
              "emoji": message.sticker.emoji, "set_name": message.sticker.set_name,
              "mask_position": message.sticker.mask_position, "file_size": message.sticker.file_size,
              "is_animated": message.sticker.is_animated}

    with open('sticker_data.json', 'w') as outfile:
         json.dump(all_stick_data, outfile)
 
 
    sticker_file_info = bot.get_file(all_stick_data.get("file_id"))
    new_sticker_file = bot.download_file(sticker_file_info.file_path)
    with open("sticker.webp", 'wb') as new_file:
        new_file.write(new_sticker_file)
    imgbp = Image.open("sticker.webp")
    imgbp.save("sticker.png", "png")
 
    import os
    os.remove("sticker.webp")
 
@bot.message_handler(content_types=['photo'])
def get_photodata(message):
    picID = message.json['photo'][-1]['file_id']
 
    file_info = bot.get_file(picID)
    new = bot.download_file(file_info.file_path)
    with open("image.png", 'wb') as new_file:
        new_file.write(new)
    os.system('waifu2x\waifu2x-ncnn-vulkan.exe -i image.png -o image2.png -n 2 -s 2')
    print("done")
    imgrsz = Image.open("image2.png")
    imgrsz.resize((512, 512)).save
    imgrsz.thumbnail((512, 512))
    imgrsz.save("image.png")
 
@bot.message_handler(commands=['addsticker'])
def start(message):
  sent = bot.send_message(message.chat.id, "Send emoji to assign it to sticker")
  bot.register_next_step_handler(sent, get_emoji)
 
def get_emoji(message):
    emoji = message.text
    sent = bot.send_message(message.chat.id, 'Now send your stiker')
    bot.register_next_step_handler(sent, getstik, emoji)
 
def getstik(message, emoji):
    if (message.content_type == 'photo'):
        get_photodata(message)
        fID = bot.upload_sticker_file(USERID, open("image.png", "rb")).file_id
        print("photo upload")
    if (message.content_type == 'sticker'):
        get_stickerid(message)
        fID = bot.upload_sticker_file(USERID, open("sticker.png", "rb")).file_id


    bot.add_sticker_to_set(
        message.chat.id,
        name=packname,
        png_sticker=fID,
        emojis=emoji
    )

    bot.send_message(message.chat.id, "Sticker has been added successfully")
 
if __name__ == '__main__':
    # start_message(message)
    bot.infinity_polling()


# 1686862883
# 1686862883