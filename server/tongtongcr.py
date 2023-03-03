# 통통이뷔페만 12시에 한번더 크롤링!
import os
import urllib
import unicodedata
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from datetime import datetime
from weekday import *


options = webdriver.ChromeOptions()
# options.add_argument("headless")


driver = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=options)


driver.get('https://www.instagram.com/')
driver.set_window_size(1500, 900)

# 해당 요소가 로딩이 완료될때까지 최대 n초 대기 하는 'Explicit Waits'
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys('ej_python2')
time.sleep(0.5)
# 기다리지 않고 그냥 가져오는 코드
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('zx0312632')
time.sleep(1)
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
driver.implicitly_wait(5)

time.sleep(0.5)
driver.find_element(
    by=By.CLASS_NAME, value='_ac8f').click()
time.sleep(0.5)
driver.implicitly_wait(5)

driver.find_element(
    by=By.CLASS_NAME, value='_a9--._a9_1').click()
time.sleep(0.5)
driver.implicitly_wait(5)

# url1 = 'https://www.instagram.com/goldenball9_mega/'
# url2 = 'https://www.instagram.com/goldenball9_smart/'
# url3 = 'https://www.instagram.com/real_jjang_3/'
# url4 = 'https://www.instagram.com/real_jjang_1/'
url5 = 'https://www.instagram.com/tongtongtong22/'
# url6 = 'https://www.instagram.com/bobdream_/'


driver.get(url5)
time.sleep(0.5)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
time.sleep(0.5)
driver.implicitly_wait(5)


url = driver.current_url
driver.get(url)
time.sleep(0.5)
driver.implicitly_wait(5)
elem = driver.find_element(
    by=By.CSS_SELECTOR, value='div._a9zs')
time.sleep(0.5)
source_code = elem.get_attribute("innerHTML")
# 스트링 가공
source_code_split_str = source_code.split('맛있게드세요')

with open('./tong_todaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code_split_str[0] + '</h1>')
    time.sleep(0.5)
f.close()
