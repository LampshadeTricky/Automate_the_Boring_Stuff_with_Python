#! python3
# imageSiteDownloader.py - Write a program that goes to a photo-sharing site 
# like Flickr or Imgur, searches for a category of photos, and then downloads 
# all the resulting images. You could write a program that works with any photo 
# site that has a search feature.

rootURL = 'https://www.flickr.com/'
saveFolder = 'C:\\Users\\jonat\\Documents\\Python\\' + \
             'Automate_the_Boring_Stuff_with_Python\\ch11'

import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get(rootURL)

searchBox = browser.find_element_by_tag_name('#search-field')
searchBox.send_keys('Testing' + Keys.ENTER)

time.sleep(5)
print(str(browser.title))
searchResults = browser.find_element_by_class_name('#yui_3_16_0_1_1596584949046_470')
print(searchResults.text)