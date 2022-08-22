from PIL import Image
import argparse
import os
import datetime
SIZE = 512

def changePixels(file):
    im = file
    # im = Image.open(file)
    im = Image.open("./waifu2x/temp/{0}".format(filename))
    nowstr = datetime.datetime.now().strftime("%H%M%S")
    im.resize((SIZE, SIZE)).save(
        "./result/{}_{}.png".format(file.replace(".png", ""),nowstr))
    print("end")

def main(args):
    # changePixels(args.file)
    changePixels(args)

if __name__ == '__main__':
    #   parser = argparse.ArgumentParser()
    # parser.add_argument("file", type=str, help="The file to break into 128x128 images")
    # args = parser.parse_args()
    # main(args)

    for filename in os.listdir("./waifu2x/temp"):
        main(filename)

    