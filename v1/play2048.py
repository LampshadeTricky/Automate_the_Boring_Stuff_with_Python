#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
gameBoard = browser.find_element_by_tag_name('html')
# tryAgain = browser.find_element_by_class_name('.retry-button')

while True:
    gameBoard.send_keys(Keys.UP)
    gameBoard.send_keys(Keys.RIGHT)
    gameBoard.send_keys(Keys.DOWN)
    gameBoard.send_keys(Keys.LEFT)
    # tryAgain.send_keys(Keys.ENTER)