from selenium import webdriver
from selenium.webdriver.common import keys
import time

lst = []
username_email = ''
user_password = ''
print("PLEASE ENSURE THAT YOU HAVE A ACTIVE INTERNET CONNECTION.\nAuthenticating.......")


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.Keys.ENTER)
        time.sleep(5)

    def likehashtags(self,hashtag):
        bot = self.bot
        hashtags = '#' + hashtag
        bot.get("https://www.instagram.com/explore/tags/"+hashtag+'/')
        time.sleep(6)
        for i in range(1, 5):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(4)
            hrefs = bot.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if 'B0A' in href]
        print(len(pic_hrefs))
        try:
            pic_hrefs = pic_hrefs[0:20]
        except:
            pass
        t = 1
        for i in pic_hrefs:
            print(t)
            t += 1
            bot.get(i)
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            try:
                time.sleep(2)
                bot.find_element_by_xpath('//span/button[@class="dCJp8 afkep _0mzm-"]').click()
                time.sleep(10)
            except Exception as e:
                time.sleep(20)

    def feedlike(self):
        bot = self.bot
        for i in range(1, 3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
        for i in range(1, 3):
            time.sleep(2)
            try:
                time.sleep(2)
                bot.find_element_by_xpath('//span/button[@label="Like"]').click()
                time.sleep(5)
                bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            except Exception as e:
                time.sleep(20)
                bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")


ask_preferences = ''

while ask_preferences != 'f' or ask_preferences != 'h':
    ask_preferences = input("do you want to like feed or certain hashtags:>(reply with f or h):> ")
    if len(ask_preferences) >= 1:
        if ask_preferences[0].lower() == 'f':
            no = InstaBot(username_email, user_password)
            time.sleep(3)
            no.login()
            no.feedlike()
            break
        elif ask_preferences[0].lower() == 'h':
            st = input("Please input your desired name or hashtag:> ")
            if len(st) >= 1:
                lst.append(st)
            for i in lst:
                ls = i
            no = InstaBot(username_email, user_password)
            time.sleep(3)
            no.login()
            no.likehashtags(ls)
            break
        else:
            print("please enter f or h")
    else:
        print("please enter f or h")
