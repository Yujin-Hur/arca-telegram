from bs4 import BeautifulSoup
import urllib.request
import time
from PIL import Image
import os


SIZE = 512
base_url = "https:"
url = "https://arca.live/e/29914"
path = "./img"

# update pixel & resolution at path directory
def enhance_image(path):
    nowstr = time.strftime("%y%m%d-%H%M%S")
    for filename in os.listdir(path):
        # waifu
        cmd = '..\waifu2x\waifu2x-ncnn-vulkan.exe -i ./img/{} -o ./result/{} -n 2 -s 2'.format(
            filename, filename)
        os.system(cmd)
        # pixel
        im = Image.open("./result/" + filename)
        im.resize((SIZE, SIZE)).save("./result/" + filename)

    print("=========== End enhance images ============== ")


def get(max_count=100):

    filename = time.strftime("%y%m%d-%H%M%S")

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    imgs = soup.find_all("img")  # 이미지 태그

    count = 1

    for img in imgs:
        if count > max_count:
            break

        print("+---------[ %d번 째 이미지 ]---------+" % count)
        img_src = img.get("src")
        img_url = base_url + img_src
        urllib.request.urlretrieve(
            img_url, "./img/{}_{}.png".format(filename, str(count)))

        count += 1  # 갯수 1 증가
    else:
        print("크롤링 종료")


# get(1)
enhance_image(path)
