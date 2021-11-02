from selenium import webdriver
from time import sleep
from ident import username, password
import pyautogui


class AutoLikeTinder():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        #bot = AutoLikeTinder()
        self.driver.get('https://tinder.com')

        sleep(2)

        login_btn = self.driver.find_element_by_xpath('//*[@id="q1529301273"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

        sleep(2)

        login_facebook_acc = self.driver.find_element_by_xpath('//*[@id="q1750641709"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        login_facebook_acc.click()

        sleep(2)

        #accept_cookies = self.driver.find_element_by_xpath('//*[@id="u_0_8_YD"]')
        #accept_cookies.click()

        sleep(2)

        #tinder window
        tinder_win = self.driver.window_handles[0]
        #login fb window
        self.driver.switch_to.window(self.driver.window_handles[1])

        sleep(2)

        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(username)

        sleep(2)

        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_input.send_keys(password)

        sleep(2)

        login_btn_fb = self.driver.find_element_by_id('loginbutton')
        login_btn_fb.click()

        sleep(2)

        #back to tinder window
        self.driver.switch_to.window(tinder_win)

        sleep(5)


        #popups tinder
        allow_loc = self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[1]')
        allow_loc.click()

        sleep(2)

        get_notification = self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[2]')
        get_notification.click()

        sleep(5)

        like_received = self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div[3]/button[2]')
        like_received.click()

        sleep(4)

    #like and dislike functions
    #def like(self):
    #    button_like = self.driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
    #    button_like.click()
    #    sleep(2)

    def dislike(self):
        button_dislike = self.driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')
        button_dislike.click()
        sleep(2)

    def autoLike(self):
        #while True:
        #    sleep(0.6)
        #    button_dislike = self.driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')
        #    button_dislike.click()
        #    sleep(0.5)
        #    #self.dislike()
        for x in range(0, 25):
            pyautogui.press('left')
            sleep(0.6)
            if x == 25:
                break
            print(x)

    def main(self):
        bot = AutoLikeTinder()
        bot.login()
        bot.autoLike()


