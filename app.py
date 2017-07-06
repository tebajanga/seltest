from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "code4tanzania", "whatsapp_db")

# Prepare a cursor object using cursor() method.
cursor = db.cursor()

config = {
    'chromedriver_path': '/usr/local/share/chromedriver',
    'get_msg_interval': 5,  # Time (seconds). Recommended value: 5
    'colors': True,  # True/False. True prints colorful msgs in console
    'ww_url': "https://web.whatsapp.com/"
}

driver = webdriver.Chrome(config['chromedriver_path'])

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## actual login in hockey app site
def whatsapp_login():
	driver.get(config['ww_url'])
	wait(40)

def do_some():
input_box = driver.find_element(By.XPATH, '//*[@id="main"]//footer//div[contains(@class, "input")]')

### Main Method
if __name__ == "__main__":
	whatsapp_login()
	wait()
    do_some()

## Try reading data.
try:
   fetch_data()
except:
   print "Error: unable to fecth data"



