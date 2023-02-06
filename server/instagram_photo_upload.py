import os
import unicodedata
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime


def upload_file(file_path, file_name):

    options = webdriver.ChromeOptions()
# options.add_argument("headless")
    driver = webdriver.Chrome(
        executable_path="./chromedriver.exe", options=options)

    driver.get('https://www.instagram.com/')
    driver.set_window_size(1500, 900)

    # 해당 요소가 로딩이 완료될때까지 최대 n초 대기 하는 'Explicit Waits'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys('nohryangbob')
    time.sleep(0.5)
    # 기다리지 않고 그냥 가져오는 코드
    driver.find_element(
        by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('zx031263')
    time.sleep(0.5)
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
