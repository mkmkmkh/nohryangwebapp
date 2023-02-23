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


# from func import *

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# # 혹은 options.add_argument("--disable-gpu")

# driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

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

url1 = 'https://www.instagram.com/goldenball9_mega/'
url2 = 'https://www.instagram.com/goldenball9_smart/'
url3 = 'https://www.instagram.com/real_jjang_3/'
url4 = 'https://www.instagram.com/real_jjang_1/'
url5 = 'https://www.instagram.com/tongtongtong22/'
url6 = 'https://www.instagram.com/bobdream_/'

# 메가점

driver.get(url1)
time.sleep(0.5)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
time.sleep(0.5)
driver.implicitly_wait(5)
# 첫번쨰 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
time.sleep(0.5)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[0], 'mega' + ".jpg")
time.sleep(0.5)

# 포스트 텍스트 크롤링

url = driver.current_url
driver.get(url)
time.sleep(0.5)
driver.implicitly_wait(5)
elem = driver.find_element(
    by=By.CSS_SELECTOR, value='div._a9zs')
time.sleep(0.5)
source_code = elem.get_attribute("innerHTML")

with open('./megatodaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code)
    time.sleep(0.5)
f.close()


# 스마트빌딩점

driver.get(url2)
time.sleep(0.5)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
time.sleep(0.5)
driver.implicitly_wait(5)

# 두번째 사진으로 클릭을통해 넘어가기
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aaqg._aaqh>button').click()
time.sleep(0.5)
driver.implicitly_wait(5)

# 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
time.sleep(0.5)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[1], 'smart' + ".jpg")
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
source_code_split_str = source_code.split('&')

with open('./smarttodaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code_split_str[0] + '</h1>')
    time.sleep(0.5)
f.close()

# 레알짱_3호점

driver.get(url3)
time.sleep(0.5)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
time.sleep(0.5)
driver.implicitly_wait(5)
# 첫번쨰 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
time.sleep(0.5)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[13], 'real' + ".jpg")

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
time.sleep(0.5)


source_code_split_str = source_code.split('&')


with open('./realtodaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code_split_str[0]+' 등' + '</h1>')
    time.sleep(0.5)
f.close()
# 요일계산후 일요일휴무를 토 밤부터 일밤까지 출력 sunday.html


# 레알짱 본점

driver.get(url4)
time.sleep(0.5)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
time.sleep(0.5)
driver.implicitly_wait(5)
# 첫번쨰 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
time.sleep(0.5)
driver.implicitly_wait(5)

t = time.localtime()
current_time = time.strftime("%H", t)

if current_time == '10' or current_time == '11':
    urllib.request.urlretrieve(img_url[13], 'real_1' + ".jpg")
else:
    urllib.request.urlretrieve(img_url[12], 'real_1' + ".jpg")
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
time.sleep(0.5)


source_code_split_str = source_code.split('#')


with open('./real_1_todaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code_split_str[0] + '</h1>')
    time.sleep(0.5)
f.close()
# 요일계산후 일요일휴무를 토 밤부터 일밤까지 출력 sunday.html


# 통통이 뷔페

driver.get(url5)
time.sleep(0.5)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
time.sleep(0.5)
driver.implicitly_wait(5)


# 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
time.sleep(0.5)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[0], 'tong' + ".jpg")
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
source_code_split_str = source_code.split('#')

with open('./tong_todaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code_split_str[0] + '</h1>')
    time.sleep(0.5)
f.close()


# 밥드림

# driver.get(url6)
# time.sleep(0.5)
# driver.implicitly_wait(5)

# # 첫번쨰 게시물 클릭s
# driver.find_element(
#     by=By.CSS_SELECTOR, value='div._aagw').click()
# time.sleep(0.5)
# driver.implicitly_wait(5)
# # 첫번쨰 이미지 소스 프린트.
# images = driver.find_elements(
#     by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
# img_url = []
# time.sleep(0.5)
# driver.implicitly_wait(5)
# # img_url = images.__getattribute__('src')

# for image in images:
#     url = image.get_attribute('src')
#     img_url.append(url)
# time.sleep(0.5)
# driver.implicitly_wait(5)

# urllib.request.urlretrieve(img_url[0], 'dream' + ".jpg")
# time.sleep(0.5)

# 포스트 텍스트 크롤링

url = driver.current_url
driver.get(url)
time.sleep(0.5)
driver.implicitly_wait(5)
elem = driver.find_element(
    by=By.CSS_SELECTOR, value='div._a9zs')
time.sleep(0.5)
source_code = elem.get_attribute("innerHTML")
# 스트링 가공
source_code_split_str = source_code.split('#')
# 파일에저장
with open('./dreamtodaymenu.html', 'w', encoding='utf-8') as f:
    time.sleep(0.5)
    f.write(source_code)
    time.sleep(0.5)
f.close()

driver.quit()

# 일요일 휴무 코드
day = t.tm_wday
if day == '6':
    with open('./sunday.html', 'w', encoding='utf-8') as f:
        time.sleep(0.5)
        f.write('<h4>일요일 휴무</h4>')
        time.sleep(0.5)
    f.close()
else:
    with open('./sunday.html', 'w', encoding='utf-8') as f:
        time.sleep(0.5)
        f.write('')
        time.sleep(0.5)
    f.close()


# for index, link in enumerate(img_url):
#     #     start = link.rfind('.')
#     #     end = link.rfind('&')
#     #     filetype = link[start:end]
#     urlretrieve(link, f'./img/{index}.jpg')


# 폴더만들고 이미지 저장

# img_folder = './img'

# if not os.path.isdir(img_folder):  # 없으면 새로 생성하는 조건문
#     os.mkdir(img_folder)

# for index, link in enumerate(img_url):
#     #     start = link.rfind('.')
#     #     end = link.rfind('&')
#     #     filetype = link[start:end]
#     urlretrieve(link, f'./img/{index}.jpg')


# 페이지 뒤로가기
# driver.execute_script("window.history.go(-2)")

# # 팝업창으로 이동/복귀
# driver.switch_to.window(driver.window_handles[1])
# driver.close()   # 각각 종료
# driver.switch_to.window(driver.window_handles[0])
# driver.close()   # 각각 종료
# # driver.switch_to.window(driver.current_window_handle)    # 현재 드라이버 포커싱 (맨 앞으로 오지는 않음)


# driver.close()   # 각각 종료
# driver.quit()    # 콘솔까지 완전 종료
