from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

### configurations
number_of_times = 1
message = 'Imejiandika Yenyewe.'

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	wait(50)

def sendMessage(msg='Hi!'):
	web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)

## quit web driver for selenium
def web_driver_quit():
	driver.quit()

### Main Method
if __name__ == "__main__":
	whatsapp_login()
	wait()
	
	for i in range(number_of_times):
		sendMessage(message)
		wait()
	print("Process complete successfully")

	wait()
	web_driver_quit()


