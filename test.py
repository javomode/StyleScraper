from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService #
from selenium.webdriver.common.by import By #to help identify elements on page
from webdriver_manager.chrome import ChromeDriverManager #webdriver to perform browser automation on real browsers
import time
import requests
import pandas as pd

service = ChromeService(executable_path="chromedriver.exe")
wd = webdriver.Chrome(service=service)

wd.get("https://youtube.com/")

input_element = wd.find_element(By.CLASS_NAME, "external-icon")


a = 0