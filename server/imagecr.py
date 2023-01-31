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

options = webdriver.ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=options)


driver.get('https://www.instagram.com/')
driver.set_window_size(1500, 900)

# 해당 요소가 로딩이 완료될때까지 최대 n초 대기 하는 'Explicit Waits'
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys('ej_python')
# 기다리지 않고 그냥 가져오는 코드
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('zxc0312')
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
driver.implicitly_wait(5)

driver.find_element(
    by=By.CLASS_NAME, value='_ac8f').click()
driver.implicitly_wait(5)

driver.find_element(
    by=By.CLASS_NAME, value='_a9--._a9_1').click()
driver.implicitly_wait(5)

url1 = 'https://instagram.com/goldenball9_mega/'
url2 = 'https://instagram.com/goldenball9_smart/'
url3 = 'https://instagram.com/real_jjang_3/'

# 메가점

driver.get(url1)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
driver.implicitly_wait(5)
# 첫번쨰 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[0], 'mega' + ".jpg")
driver.implicitly_wait(5)

# 메뉴 텍스트 불러오기


# 메뉴str 텍스트파일에 저장
with open('mega.txt', 'w') as f:
    try:
        f.write(menu_str)
    except:
        pass


# 스마트빌딩점

driver.get(url2)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
driver.implicitly_wait(5)

# 두번째 사진으로 클릭을통해 넘어가기
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aaqg._aaqh>button').click()
driver.implicitly_wait(5)

# 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[1], 'smart' + ".jpg")
driver.implicitly_wait(5)


# 레알짱

driver.get(url3)
driver.implicitly_wait(5)

# 첫번쨰 게시물 클릭s
driver.find_element(
    by=By.CSS_SELECTOR, value='div._aagw').click()
driver.implicitly_wait(5)
# 첫번쨰 이미지 소스 프린트.
images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
img_url = []
driver.implicitly_wait(5)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
driver.implicitly_wait(5)

urllib.request.urlretrieve(img_url[0], 'real' + ".jpg")
driver.implicitly_wait(5)

driver.close()

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
