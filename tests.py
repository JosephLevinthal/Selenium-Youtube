#Import section
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Declare path for webdriver
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

# Access Home Page
website = 'https://youtube.com.br'
driver.get(website)

# Access trending page
time.sleep(3)
website = 'https://www.youtube.com/feed/trending'
driver.get(website)

