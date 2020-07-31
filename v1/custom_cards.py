#! python3
# custom_cards.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 17 Project

import os
from PIL import Image, ImageDraw, ImageColor, ImageFont

baseWidth, baseHeight = 360, 288
os.chdir('c:\\users\\jonat\\documents\\python\\sandbox')

def make_cards(guestList):
    """Makes custom cards for each guest
    Args:
        guestList (str): Path to file containing guest list
    Returns:
        None
    """
    # make folder to store resulting images
    os.makedirs('imageCards', exist_ok=True)

    # load flower image
    flowerWidth, flowerHeight, flowerImg = createBaseImage('flower.jpg')

    # read each guest from file
    with open(guestList) as file:
        for line in file:
            guest = line[:-1]

            # create image
            card = Image.new('RGBA', (baseWidth, baseHeight), 'white')
            # add flower image
            card.paste(flowerImg, (0, int(baseHeight / 2) - int(flowerHeight / 2), ))

            # create border around image
            border = Image.new('RGBA', (363, 291), 'black')
            border.paste(card, (3,3))

            # draw guest name
            draw_obj = ImageDraw.Draw(border)
            card_font = ImageFont.truetype('calibri.ttf', 24)
            draw_obj.text((100, 0), guest, fill='Black', font=card_font)

            # save resulting image
            imageName = '{}_card.png'.format(guest)
            border.save(os.path.join('imageCards', imageName))
    

def createBaseImage(fileName):
    bgImage = Image.open('.\\' + fileName)
    bgWidth, bgHeight = bgImage.size

    # Resize background image to fit inside the required size
    if bgWidth > baseWidth:
        bgHeight = int(baseWidth / bgWidth * bgHeight)
        bgWidth = baseWidth
    else:
        bgWidth = int(baseHeight / bgHeight * bgWidth)
        bgHeight = baseHeight

    bgImage.thumbnail((bgWidth, bgHeight))

    return bgWidth, bgHeight, bgImage

if __name__ == "__main__":
    make_cards('guests.txt')