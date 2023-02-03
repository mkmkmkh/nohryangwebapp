from fileinput import close
import os
import urllib
import unicodedata
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from func import *


# def instagram_text_download():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(
#         executable_path="./chromedriver.exe", options=options)
#     # 3 ID's instagram_last_post_text_download
#     txts = driver.find_elements(
#         by=By.CSS_SELECTOR, value='h1._aacl _aaco _aacu _aacx _aad7 _aade')
#     txt_url = []
#     time.sleep(0.5)
#     driver.implicitly_wait(5)

#     for txt in txts:
#         url = txt.text
#         txt_url.append(url)
#     time.sleep(0.5)
#     driver.implicitly_wait(5)

#     with open('mega.txt', 'w') as f:
#         f.write(txt_url[0])

#     close('mega.txt')
