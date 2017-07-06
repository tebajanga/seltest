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
	wait(5)

def fetch_data():
    # Execute the SQL command
   cursor.execute("SELECT * from inbox where id > 14")
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      sms_id = row[0]
      sms_type = row[1]
      sms_sender = row[2]
      sms_body = row[3]
      sms_processed = row[4]

      # Now print fetched result
      print "Sending to =%s \n" % (sms_sender)

      # Now sending.
      chooseReceiver("Henry!")

### Main Method
if __name__ == "__main__":
	whatsapp_login()
	wait()

## Try reading data.
try:
   fetch_data()
except:
   print "Error: unable to fecth data"



