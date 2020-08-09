#! python3
# 2048.py - 2048 is a simple game where you combine tiles by sliding them up, 
# down, left, or right with the arrow keys. You can actually get a fairly high 
# score by repeatedly sliding in an up, right, down, and left pattern over and 
# over again. Write a program that will open the game at 
# https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and 
# left keystrokes to automatically play the game.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# Wait a few seconds to dismiss the stupid cookie message
time.sleep(5)
browser.find_element_by_tag_name('.cookie-notice-dismiss-button').click()

# Find the gameboard
gameBoard = browser.find_element_by_tag_name('html')

while True:
    gameBoard.send_keys(Keys.UP)
    gameBoard.send_keys(Keys.RIGHT)
    gameBoard.send_keys(Keys.DOWN)
    gameBoard.send_keys(Keys.LEFT)

    # if the game is over, click the retry button
    retryButton = browser.find_element_by_tag_name('.retry-button')
    if retryButton.location['x'] > 0:
        retryButton.click()