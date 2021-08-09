import matplotlib.pyplot as plt
import calendar
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from urllib3.packages.six import b
from matplotlib.font_manager import FontProperties

webURL = "https://popcat.click/?fbclid=IwAR2X75yQgQDUjp7EJeZwxJVpCw_mdJt0yDc8zJ67f9OsDVSKDRHZH2Som7A"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(webURL)
driver.set_window_size(400,400)

element = driver.find_element_by_class_name("cat-img.p")
while True:
    element.click()
    time.sleep(0.01)

driver.quit()