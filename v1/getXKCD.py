#! python3

import requests, bs4, os

saveFolder = 'C:\\Users\\jonat\\Documents\\Python\\Sandbox\\xkcd'

def getTargetURL(theURL, theType):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 ' + \
        '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }    
    res = requests.get(theURL, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    if theType.lower() == 'image':
        elems = soup.select('#comic')    
        targetURL = 'http:' + elems[0].contents[1].attrs['src']
    elif theType.lower() == 'prev':
        elems = soup.select('#middleContainer > ul:nth-child(2) > li:nth-child(2) > a')    
        targetURL = 'http://xkcd.com' + elems[0].attrs['href']
    else:
        # This will probably break the program
        targetURL = ''
    return targetURL

def getComicImage(theURL):
    targetURL = getTargetURL(theURL, 'image')
    theImage = requests.get(targetURL)
    folderName = saveFolder
    fileNameSplit = targetURL.split('/')
    fileName = fileNameSplit[-1]
    print('Retrieving file: ' + fileName)

    os.chdir(folderName)

    file = open(fileName, 'wb')
    file.write(theImage.content)
    file.close()

def getNextURL(theURL):
    targetURL = getTargetURL(theURL, 'prev')
    return targetURL

# Main Program
currentURL = 'http://www.xkcd.com'

print('Retrieving images from ' + currentURL)

for i in range(1, 10):
    getComicImage(currentURL)
    currentURL = getNextURL(currentURL)

print('Done.')