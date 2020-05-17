from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy

class TwitterBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        try:
            Twitter = WebDriverWait(driver, 10).until(
                self.driver.get("https://Twitter.com/login")
            )
        
            self.driver.find_element_by_xpath("//input[@name=\'session[username_or_email]\']").send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\'session[password]\']").send_keys(password)

            Login = WebDriverWait(driver, 10).until(
                self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div")\
            .click()
            )
        except:
            self.driver.quit()
        
    def _getUserList(self, url):
        self.driver.get(url.format(self.username))
        time.sleep(3)
        previousHeight = 1
        currentHeigh = 2
        while (previousHeight != currentHeigh):
            previousHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, " + str(previousHeight) + ");")
            time.sleep(0.5)
            currentHeigh = self.driver.execute_script("return document.documentElement.scrollHeight")

        data = self.driver.find_elements_by_class_name('css-16my406')
        contentText = [contents.text for contents in data if contents.text != '']
        users = []
        for x in range(len(contentText)):
            if ord(contentText[x][:1]) == 64:
                users.append(contentText[x])

        return users

    def getUnfollows(self):
        following = self._getUserList("https://twitter.com/{0}/following")
        followers = self._getUserList("https://twitter.com/{0}/followers")
        notFollowingBack = [user for user in following if user not in followers]

        return notFollowingBack

    def likePost(self, hashtag):
        searchBox = self.driver.find_element_by_id("SearchBox_Search_Input")
        searchBox.send_keys(hashtag)
        try:
            Search = WebDriverWait(driver, 10).until(
                searchBox.send_keys(Keys.Enter)
            )
            timeline = self.driver.find_element_by_class("css-1dbjc4n")
            tweets = timeline.find_element_by_class("css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll")
            for tweet in tweets:
                like = tweet.find_element_by_id("like")
                like.click

        except:
            self.driver.quit()
    

