from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/usr/local/share/chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 60)
 
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"+255 766 266 161"'
 
# Replace the below string with your own message
string = "Message - lol "
 
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)