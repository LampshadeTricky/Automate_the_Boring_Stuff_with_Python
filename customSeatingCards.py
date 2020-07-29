#! python3

import os
from PIL import Image, ImageColor, ImageFont

baseWidth, baseHeight = 360, 288
os.chdir('c:\\users\\jonat\\documents\\python\\sandbox')
    
# TODO: Create base image from blank background and flower image.
def createBaseImage(fileName):
    baseImage = Image.new('RGBA', (baseWidth, baseHeight), ImageColor.getcolor('Black','RGBA'))

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

    baseImage.paste(bgImage, (0, int(baseHeight / 2) - int(bgHeight / 2), ))

    return baseImage



createBaseImage('flower.jpg').save('baseImage.png')

# TODO: Open guests.txt, get guest list and close file.

# TODO: Loop through guests and create new images.
try:
    os.mkdir('.\\seating_cards')
except:
    pass

os.chdir('.\\seating_cards')

