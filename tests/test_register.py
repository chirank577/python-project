from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_important_field(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("chiru")
        self.driver.find_element(By.ID, "input-lastname").send_keys("singh")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("512222756")
        self.driver.find_element(By.ID, "input-password").send_keys(12345)
        self.driver.find_element(By.ID, "input-confirm").send_keys(12345)
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        sleep(5)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text ==("Your Account Has Been Created!")
        sleep(3)


    def test_register_with_all_field(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("chiru")
        self.driver.find_element(By.ID, "input-lastname").send_keys("singh")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("512222756")
        self.driver.find_element(By.ID, "input-password").send_keys(12345)
        self.driver.find_element(By.ID, "input-confirm").send_keys(12345)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        sleep(5)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text == ("Your Account Has Been Created!")
        sleep(3)


    def test_create_an_account_with_existing_emial(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("chiru")
        self.driver.find_element(By.ID, "input-lastname").send_keys("singh")
        self.driver.find_element(By.ID, "input-email").send_keys('chirank577@gmail.com')
        self.driver.find_element(By.ID, "input-telephone").send_keys("512222756")
        self.driver.find_element(By.ID, "input-password").send_keys(12345)
        self.driver.find_element(By.ID, "input-confirm").send_keys(12345)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        sleep(5)
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__ ("Warning: E-Mail Address is already registered!")
        sleep(3)


    def test_register_without_any_input(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("")
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        self.driver.find_element(By.ID, "input-email").send_keys('')
        self.driver.find_element(By.ID, "input-telephone").send_keys('')
        self.driver.find_element(By.ID, "input-password").send_keys()
        self.driver.find_element(By.ID, "input-confirm").send_keys()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_first_name_warning='First Name must be between 1 and 32 characters!'
        assert self.driver.find_element(By.CSS_SELECTOR,'input#input-firstname+div').text.__contains__ (expected_first_name_warning)
        expected_lastname_warning='Last Name must be between 1 and 32 characters!'
        assert self.driver.find_element(By.CSS_SELECTOR, 'input#input-lastname+div').text.__contains__ (expected_lastname_warning)

        sleep(5)



    def generate_email_with_stamp(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "chiru"+time_stamp+"@gmail.com"

