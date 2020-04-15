from selenium import webdriver
import time
import numpy
class TwitterBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get("https://Twitter.com/login")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\'session[username_or_email]\']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\'session[password]\']").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div")\
            .click()
        time.sleep(3)

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
        notFollowingBack =[user for user in following if  user not in followers]
        return notFollowingBack



f = open("password.txt", "r")
password = f.read()
bot = TwitterBot("username here", password)
notFollowingBack = bot.getUnfollows()
print(notFollowingBack)



