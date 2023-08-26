from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import string

class TrademarkBot:
    
    def __init__(self):
        self.driver = self.init_driver()

    def init_driver(self):
        chrome_driver_path = "Users/vedantvyas/Downloads/chromedriver"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--log-path=chromedriver.log")
        return webdriver.Chrome(options=chrome_options)

    def check_availability(self, trademark):
        search_url = f"https://ised-isde.canada.ca/cipo/trademark-search/srch?payload=%257B%2522domIntlFilter%2522%253A%25221%2522%252C%2522searchfield1%2522%253A%2522all%2522%252C%2522textfield1%2522%253A%2522{trademark}%2522%252C%2522display%2522%253A%2522list%2522%252C%2522maxReturn%2522%253A%2522500%2522%252C%2522nicetextfield1%2522%253Anull%252C%2522cipotextfield1%2522%253Anull%257D&pageNum=0&pageLen=1000"
        self.driver.get(search_url)

        try:
            self.driver.find_element_by_class_name("result")
        except Exception as e:
            if "Timed out" in str(e):
                print("Timed out waiting for page to load")
            return False

        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        results = soup.find_all("div", class_="result")

        for result in results:
            if "Available" in result.get_text():
                return True
        return False

    def generate_similar_name(self, trademark):
        # Generate a randomized similar name
        random_suffix = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        return trademark + random_suffix

    def interact(self):
        while True:
            user_input = input("Enter a trademark name: ")
            if user_input.lower() == "exit":
                break

            availability = self.check_availability(user_input)
            if availability:
                print("Trademark is available.")
            else:
                print("Trademark is not available.")
                suggested_name = self.generate_similar_name(user_input)
                print("Suggested similar name:", suggested_name)

    def cleanup(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = TrademarkBot()
    try:
        bot.interact()
    finally:
        bot.cleanup()
