#!/usr/bin/python3

# Taking Website Screenshots using selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

arg = sys.argv[1]
driver = webdriver.Firefox()
driver.get(arg)

H = driver.execute_script("return document.body.scrollHeight")
W = driver.execute_script("return document.body.scrollWidth")

driver.set_window_size(W, H)
driver.find_element(By.TAG_NAME, "body")
driver.save_screenshot('screenshot.png')
