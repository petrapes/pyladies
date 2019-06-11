from selenium import webdriver
from locators import Locators
import time
from selenium.common.exceptions import NoSuchElementException

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.follow_button_xpath = Locators.follow_button_xpath
        self.following_button_xpath = Locators.following_button_xpath
        self.end_following_confirm_xpath = Locators.end_following_confirm_xpath

    def follow_with_username(self, username):
        try:
            followButton = self.driver.find_element_by_xpath(self.follow_button_xpath)
            followButton.click()
            time.sleep(5)
        except NoSuchElementException:
            time.sleep(5)
            print("You are already following this user")

    def unfollow_with_username(self, username):
        try:
            followingButton = self.driver.find_element_by_xpath(self.following_button_xpath)
            followingButton.click()
            time.sleep(2)
            confirmButton = self.driver.find_element_by_xpath(self.end_following_confirm_xpath)
            confirmButton.click()
            time.sleep(5)
        except NoSuchElementException:
            time.sleep(5)
            print("You are not following this user")
