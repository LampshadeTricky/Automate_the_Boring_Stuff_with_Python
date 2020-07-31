#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads

import requests, os, bs4, threading

saveFolder = 'C:\\Users\\jonat\\Documents\\Python\\Sandbox\\xkcd'
os.chdir(saveFolder)

def downloadXKCD(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        if urlNumber == 0: continue
        # Download the page.
        statusMessage = f'Downloading page http://xkcd.com/{urlNumber} --> '
        try:
            thePage = requests.get(f'http://xkcd.com/{urlNumber}')
            thePage.raise_for_status()            
        except requests.exceptions.HTTPError:
            statusMessage += 'HTTPError'
            continue
        except requests.exceptions.InvalidURL:
            statusMessage += 'Invalid URL'
            continue

        soup = bs4.BeautifulSoup(thePage.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic')
        if comicElem == []:
            statusMessage += 'No image found'
        else:
            try:
                imageURL = 'http:' + comicElem[0].contents[1].attrs['src']
                theImage = requests.get(imageURL)
                fileNameSplit = imageURL.split('/')
                fileName = fileNameSplit[-1]
                
                file = open(fileName, 'wb')
                file.write(theImage.content)
                file.close()
                statusMessage = ''
            except KeyError:
                statusMessage += 'KeyError'

        if len(statusMessage) > 0:
            print(statusMessage)

downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXKCD, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')