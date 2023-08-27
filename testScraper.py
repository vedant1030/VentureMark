from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from element_manager import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(ChromeDriverManager().install())
# to open the url in browser
driver.get('https://ised-isde.canada.ca/cipo/trademark-search/srch?lang=eng')

# to select the option
select_element=driver.find_element(By.XPATH,get_xpath(driver,'SvqW4HEINzAidQV'))
selecttag=Select(select_element)
selecttag.select_by_value('tmlookup_ext')

# to click on input field
driver.find_element(By.XPATH,get_xpath(driver,'34l07HUMse100gE')).click()


# to type content in input field
user_input = input("Enter a trademark name: ")
driver.find_element(By.XPATH,get_xpath(driver,'5okNS1Bdar56Q2g')).send_keys(user_input)

# press Enter key
driver.switch_to.active_element.send_keys(Keys.ENTER)

# to click on the element(Results found:      ...) found
driver.find_element(By.XPATH,get_xpath(driver,'5cw651yVMQThGHK')).click()

# to fetch the text of element
text=driver.find_element(By.XPATH,get_xpath(driver,'8JnrT9WwUitjjLl')).text
if (text == "0"):
    print("this trademark is available")
else:
    print("This trademark is unavailable")
