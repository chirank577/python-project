import pytest
from selenium import webdriver
from utilities import Readconfig



@pytest.fixture()
def setup_and_teardown(request):
   broswer=Readconfig.read_config("basic info","browser")
   driver=None
   if broswer.__eq__("chrome"):
      driver=webdriver.Chrome()
   elif broswer.__eq__("firefox"):
      driver=webdriver.Firefox()
   elif broswer.__eq__("edge"):
      driver=webdriver.Edge()
   else:
      print("provide a valid browser name from this list chrome/firefox/edge")

   driver.maximize_window()
   app_url=Readconfig.read_config("basic info","url")
   driver.get(app_url)
   request.cls.driver = driver
   yield
   driver.quit()