from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

   def test_search_for_a_product(self):

      self.driver.find_element(By.NAME, "search").send_keys("hp")
      self.driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default.btn-lg").click()
      assert self.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()


   def test_search_for_an_invalid_product(self):

      self.driver.find_element(By.NAME, "search").send_keys("honda")
      self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg").click()
      Expected_result="Products meeting the search criteria"
      assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::h2").text.__eq__(Expected_result)


   def test_search_for_no_product(self):

      self.driver.find_element(By.NAME, "search").send_keys("")
      self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg").click()
      expected_result="There is no product that matches the search criteria."
      assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_result)