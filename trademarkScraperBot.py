from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from element_manager import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TrademarkScraper:
    def __init__(self):
        self.driver = self.init_driver()
        self.open_trademark_search_page()

    def init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--log-path=chromedriver.log")
        return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def open_trademark_search_page(self):
        self.driver.get('https://ised-isde.canada.ca/cipo/trademark-search/srch?lang=eng')
        select_element = self.driver.find_element(By.XPATH, get_xpath(self.driver, 'SvqW4HEINzAidQV'))
        selecttag = Select(select_element)
        selecttag.select_by_value('tmlookup_ext')
        self.driver.find_element(By.XPATH, get_xpath(self.driver, '34l07HUMse100gE')).click()

    def check_trademark_availability(self, trademark):
        input_element = self.driver.find_element(By.XPATH, get_xpath(self.driver, '5okNS1Bdar56Q2g'))
        input_element.clear()
        input_element.send_keys(trademark)
        input_element.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, get_xpath(self.driver, '5cw651yVMQThGHK')).click()
        text = self.driver.find_element(By.XPATH, get_xpath(self.driver, '8JnrT9WwUitjjLl')).text
        if text == "0":
            return True
        else:
            return False

    def cleanup(self):
        self.driver.quit()

def main():
    bot = TrademarkScraper()
    try:
        while True:
            user_input = input("Enter a trademark name (or 'exit' to end): ")
            if user_input.lower() == "exit":
                break
            
            availability = bot.check_trademark_availability(user_input)
            if availability:
                print("Trademark is available.")
            else:
                print("Trademark is not available.")
    finally:
        bot.cleanup()

if __name__ == "__main__":
    main()
