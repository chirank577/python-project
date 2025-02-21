from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_valid_credential(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.ID,"input-email").send_keys("chirank577@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("12345678")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected='My Account'
        assert self.driver.find_element(By.XPATH, "//h2[text()='My Account']").text.__eq__(expected)

    def test_login_invalid_email_and_valid_password(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_with_stamp())
        self.driver.find_element(By.ID,"input-password").send_keys("12345678")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message="Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible").text.__eq__(expected_warning_message)

    def generate_email_with_stamp(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "chiru"+time_stamp+"gmail.com"

    def test_login_valid_email_and_invalid_password(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.ID,"input-email").send_keys("chirank577@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("123456")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible").text.__eq__("Warning: No match for E-Mail Address and/or Password.")
        sleep(5)
    def test_login_with_empty_credentials(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        self.driver.find_element(By.ID,"input-email").send_keys("")
        self.driver.find_element(By.ID,"input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible").text.__eq__("Warning: No match for E-Mail Address and/or Password.")

