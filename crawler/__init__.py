from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://www.tgju.org/currency"

class PageHandler:
    def __init__(self, url=URL, browser="chrome"):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        
    def get_info(self):
        dollar_price = self.driver.find_element(by=By.XPATH, value="//tr[@data-market-row='price_dollar_rl']/td[@class='nf']").text
        euro_price = self.driver.find_element(by=By.XPATH, value="//tr[@data-market-row='price_eur']/td[@class='nf']").text
        return {'dollar':dollar_price, 'euro':euro_price}


