from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from LoginPage import Page
from locators import Locators

class FollowersPage(Page):

    def __init__(self, driver):
        self.driver = driver

        self.followers_link_xpath = Locators.followers_link_xpath

    def getUserFollowers(self, username, max):
        self.push("//ul[contains(@class,'k9GMp')]//li[2]//a[1]")
        followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.driver)
        
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers