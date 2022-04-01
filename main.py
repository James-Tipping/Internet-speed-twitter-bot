from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

TWITTER_EMAIL = "****"
TWITTER_PASSWORD = "****"
TWITTER_USERNAME = "****"
chrome_driver_filepath = "/Users/jamestipping/Documents/Python practise/chromedriver-2"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_filepath)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speedof.me")

        accept_cookies_button = self.driver.find_element_by_css_selector(".cc-accept-btn.cc-dismiss")
        accept_cookies_button.click()

        start_button = self.driver.find_element_by_id("start_test_btn")
        start_button.click()

        time.sleep(70)

        download_speed = self.driver.find_element_by_css_selector(".meter-group text")
        print(download_speed.text)
        self.down = float(download_speed.text)

        upload_speed = self.driver.find_elements_by_css_selector(".meter-group text")[1]
        print(upload_speed.text)
        self.up = float(upload_speed.text)

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")
        time.sleep(5)
        sign_in_button = self.driver.find_element_by_xpath("//span[text()='Sign in']")
        sign_in_button.click()
        time.sleep(5)

        use_email_button = self.driver.find_element_by_xpath("//span[text()='Use your phone number, email address or username']")
        use_email_button.click()
        time.sleep(5)

        email_input = self.driver.find_element_by_name("username")
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)


        try:
            password_input = self.driver.find_element_by_name("password")
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username_input = self.driver.find_element_by_name("text")
            username_input.send_keys(TWITTER_USERNAME)
            username_input.send_keys(Keys.ENTER)
            time.sleep(5)
            password_input = self.driver.find_element_by_name("password")
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)

        time.sleep(5)

        text = f"""
Speed test conducted in Shenzhen recorded speeds of:
Upload: {self.up}
Download: {self.down}
#wannaflixvpn #wannaflix
        """

        text_box = self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block")
        text_box.click()
        text_box.send_keys(text)

        time.sleep(5)

        tweet_button = self.driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div")
        tweet_button.click()




bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()




























