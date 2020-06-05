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
wait = WebDriverWait(driver, 10)

# Access Home Page
website = 'https://youtube.com.br'
driver.get(website)

# Access trending page
time.sleep(3)
website = 'https://www.youtube.com/feed/trending'
driver.get(website)

# Access gaming page
time.sleep(3)
website = 'https://www.youtube.com/gaming'
driver.get(website)

# Search for Hefesto video
time.sleep(3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
video = 'Hefesto'
driver.get("https://www.youtube.com/results?search_query=" + str(video))

# play the first video
time.sleep(3)
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()