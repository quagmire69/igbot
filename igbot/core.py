#!/usr/bin/env python3

import time
import random

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except Exception as e:
    print(' e:', e)


class IGBot:
    
    def __init__(self, username, password):
        self.domain   = "https://instagram.com/"
        self.username = username
        self.password = password
        self.driver   = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()
        print("\n - Close")
    
    def login(self):
        driver = self.driver
        driver.get(self.domain + "accounts/login/")
        time.sleep(2)

        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)

        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def hashtag(self, tag, num_img):
        driver = self.driver
        driver.get(self.domain + "explore/tags/" + tag)
        time.sleep(2)
        
        links   = []
        while len(links) < num_img:
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                hrefs = driver.find_elements_by_tag_name('a')
                hrefs = [elem.get_attribute('href') for elem in hrefs 
                        if '.com/p/' in elem.get_attribute('href')]
                links.extend([elem for elem in hrefs if elem not in links])
                num_links = len(links)
                print(" - Gathering {}/{} photos with hashtag #{}".format(num_img, num_links, tag), end='\r')
            except Exception as e:
                print(' e:', e)
                continue

        print("\n - Liking photos ...", end="\r")
        for i in range(0, num_img):
            driver.get(links[i])
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                time.sleep(random.randint(2, 4))
                driver.find_element_by_class_name("coreSpriteHeartOpen").click()
                print(" - #{} | {} photos left.".format(tag, num_img), end='\r')
                time.sleep(1)
                num_img -= 1
            except Exception as e:
                print(' e:', e)
                time.sleep(1)

