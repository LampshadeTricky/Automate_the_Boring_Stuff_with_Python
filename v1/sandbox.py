#! python3

import os, shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Sleepy', 'Happy']