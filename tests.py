#Import section
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CenariosYoutube(unittest.TestCase):
    def setUp(self):
        #Declare path for webdriver
        self.PATH = "chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    #Access Home Page
    def test_1_test_home_page(self):
        website = 'https://youtube.com.br'
        self.driver.get(website)
        time.sleep(5)

    #Access trending page
    def test_2_test_trending(self):
        website = 'https://www.youtube.com/feed/trending'
        self.driver.get(website)
        time.sleep(5)


    #Access gaming page
    def test_3_test_gaming(self):
        website = 'https://www.youtube.com/gaming'
        self.driver.get(website)
        time.sleep(5)


    #Search for Hefesto and Play the first video
    def test_4_test_play_video(self):
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        video = 'Hefesto'
        self.driver.get("https://www.youtube.com/results?search_query=" + str(video))
        self.wait.until(visible((By.ID, "video-title")))
        self.driver.find_element_by_id("video-title").click()
        time.sleep(5)

    #Search for 'Teste de software' video
    def test_5_test_search_video(self):
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        video = 'Teste de software'
        self.driver.get("https://www.youtube.com/results?sp=mAEB&search_query=" +str(video))
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()