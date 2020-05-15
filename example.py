from TwitterClass import TwitterBot

f = open("password.txt", "r")
password = f.read()
username = "username"
bot = TwitterBot(username, password)
notFollowingBack = bot.getUnfollows()
print(notFollowingBack)