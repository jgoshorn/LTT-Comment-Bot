import os
import time
import random
import login
import numpy as np
from bs4 import BeautifulSoup, StopParsing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from random import randint, randrange
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.youtube.com/c/LinusTechTips/videos')
def login(email, password):
    
    email_input = browser.find_element_by_xpath('//*@id="idenfifierId"]')
    email_input.send_keys(email)
    browser.find_element_by_id("identifierNext").click()
    time.sleep(5)
    print("email done")
    
    password_input = (By.XPATH, '//*[@id="password"]/div/div[1]/input')
    WebDriverWait(browser, 50).until(EC.presence_of_element_located(password_input))
    input_field = browser.find_element(*password_input)
    WebDriverWait(browser,50).until(
        EC.element_to_be_clickable(password_input))
    input_field.send_keys(password)
    browser.find_element_by_id("passwordNext").click()
    time.wait(5)
    print('password done')
    WebDriverWait(browser,200).until(EC.presence_of_element_located(By.CSS_SELECTOR, "ytd-masthead button#avatar-btn"))
    
    return browser
    
    
''' email = email_input
    for i in email:
        email_input.send_keys(i)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)
        
    next_button = browser.find_elements_by_css_selector("button")
    time.sleep(2)
    next_button[2].click()
    time.sleep(2)
    
    password_input = browser.find_element_by_css_selector('input[type=password')
    password = password_input
    for i in password:
        password_input.send_keys(i)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)
        
    next_button = browser.find_elements_by_css_selector("button")
    time.sleep(2)
    next_button[2].click()
    
    confirm_button = browser.find_elements_by_css_selector("div[role=button]")
    time.sleep(2)
    if(len(confirm_button)>0):
        confirm_button[1].click()'''
    
    
'''def click_agree(browser):
    agree_button = browser.find_element_by_css_selector('button')
    time.sleep(2)
    agree_button.click()
        

    sign_in_buttons = browser.find_elements_by_css_selector('.signin')
    time.sleep(6)
    while(len(sign_in_buttons)==0):
        sign_in_buttons = browser.find_elements_by_css_selector('.signin')
        time.sleep(1)
            
        
thumbnails = browser.find_elements_by_css_selector('ytd-video-renderer')
for i in range(1,100):
    thumbnails[i].click()'''


def create_comment(browser, comment):
    
    comment_box = EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#placeholder-area'))
    WebDriverWait(browser, 4).until(comment_box)
    
    comment_input = browser.find_element_by_css_selector('#placeholder-area')
    ActionChains(browser).move_to_element(comment_input).click(comment_input).perform()
    
    add_comment = browser.find_element_by_css_selector('#contenteditable-root')
    add_comment.send_keys(comment)
    browser.find_element_by_css_selector('#submit-button').click()
    print('commented')
    
    time.sleep(5)
    
    return create_comment(browser, random_comment())

# comments need added to file 
def random_comment():
    f = open('comments.txt').read().splitlines()
    line = random.choice(f)
    return line
    
   
  #  f = next(file)
  #  for i, file in enumerate(file, 2):
  #      if random.randrange(i):
  #          continue
  #      f = file
  #  return f
  

if __name__ == '__main__':
    email = login.email
    password = login.password
    
    browser = login(email, password)
    
    while True:
        key = browser.find_element_by_name('https://www.youtube.com/c/LinusTechTips/videos')
        
        create_comment(browser, random_comment())
