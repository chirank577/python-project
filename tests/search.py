from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def test_search_for_a_product():
   driver=webdriver.Chrome()
   driver.maximize_window()
   driver.get("https://www.tutorialsninja.com/demo/")
   driver.find_element(By.NAME, "search").send_keys("hp")

