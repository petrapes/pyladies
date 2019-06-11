from selenium import webdriver
import time
import user_data
import unittest
import HtmlTestRunner
from LoginPage import LoginPage
from HomePage import HomePage
from locators import Locators

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:/Users/Peťule/Downloads/geckodriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def test_1login_and_logout(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        driver.find_element_by_xpath(Locators.signin_button_xpath).click()

        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        login.logout()
    
    def test_2follow_user(self):
        driver = self.driver
        username = "transformers_42"
        driver.get("https://www.instagram.com/" + username + "/")
        
        time.sleep(2)
        driver.find_element_by_xpath(Locators.again_login_button_xpath).click()
        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        homepage = HomePage(driver)
        homepage.follow_with_username(username)

    def test_3unfollow_user(self):
        driver = self.driver
        username = "transformers_42"
        driver.get("https://www.instagram.com/" + username + "/")
        
        time.sleep(2)
        driver.find_element_by_xpath(Locators.again_login_button_xpath).click()
        login = LoginPage(driver)
        login.enter_username(user_data.username)
        login.enter_password(user_data.password)
        login.click_login()
        homepage = HomePage(driver)
        homepage.unfollow_with_username(username)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Peťule/pyladies/selenium/reports"))

