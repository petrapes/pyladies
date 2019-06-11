from locators import Locators
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.click_following_xpath = Locators.click_following_xpath
        self.profile_link_xpath = Locators.profile_link_xpath
        self.options_link_xpath = Locators.options_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)
    
    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        time.sleep(5)

    def logout(self):
        self.driver.find_element_by_xpath(self.click_following_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.profile_link_xpath).click()
        self.driver.find_element_by_xpath(self.options_link_xpath).click()
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
        time.sleep(5)