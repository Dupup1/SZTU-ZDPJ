#!/usr/bin/python3
# *coding=utf-8* #

from seleniums import *
from time import sleep

import json


def login(driver):
    try:
        with open('./xh_pass.json',mode='r',encoding='utf-8') as f: # load xuehao and password
            jsonContent = json.load(f)
    except Exception:
        with open('./xh_pass.json',mode='w+',encoding='utf-8') as f: # if not exsist, create one
            f.write('{\n')
            f.write('\t"xuehao": "",\n')
            f.write('\t"password": ""\n')
            f.write('}\n')
        from os import getcwd
        path = getcwd().replace('\\','/')
        print(f'Please write down your xuehao and password in {path}/xh_pass.json')
        exit()
    driver.get('https://auth.sztu.edu.cn/idp/authcenter/ActionAuthChain?entityId=home')
    driver.find_element(By.XPATH,'//*[@id="j_username"]').send_keys(jsonContent['xuehao'])
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="j_password"]').send_keys(jsonContent['password'])
    driver.find_element(By.XPATH,'//*[@id="loginButton"]').click()
    sleep(3)
    driver.get('http://jwxt.sztu.edu.cn/')

if __name__ == '__main__':
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    login(driver)