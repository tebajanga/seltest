from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import MySQLdb
 
# Replace below path with the absolute path
# to chromedriver in your computer
<<<<<<< HEAD
#driver = webdriver.Chrome('/usr/local/share/chromedriver')
=======
driver = webdriver.Chrome('/usr/local/share/chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 60)
 
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"+255 766 266 161"'
>>>>>>> 7944fdf8fd18cfc15c734ac2dc0727b3cd824693
 
#driver.get("https://web.whatsapp.com/")
#wait = WebDriverWait(driver, 10)

db = MySQLdb.connect("localhost", "root", "code4tanzania", "whatsapp_db")
cursor = db.cursor()

def do_some():
    try:
# Execute the SQL command
    cursor.execute("SELECT * FROM inbox")
# Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        sms_id = row[0]
        sms_type = row[1]
        sms_sender = row[2]
        sms_body = row[3]
        sms_processed = row[4]
        sms_processed_at = row[5]
        sms_created_at = row[6]
        
        # Now print fetched result
        print   "Sender: \n" % (sms_sender)
except:
    print "Error: unable to fecth data"

### Main Method
if __name__ == "__main__":
    do_some()

#target = '"+255 765 563 474"'

# Replace the below string with your own message
#string = "Message - lol "
 
<<<<<<< HEAD
#x_arg = '//span[contains(@title,' + target + ')]'
#group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
#group_title.click()
#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
#input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

#for i in range(1):
#    input_box.send_keys(string + Keys.ENTER)
#    time.sleep(1)
=======
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
>>>>>>> 7944fdf8fd18cfc15c734ac2dc0727b3cd824693
