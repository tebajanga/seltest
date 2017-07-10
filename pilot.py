import sched
import sys
import threading
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException as WebDriverException
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException

import urllib.request as urllib2
import json

config = {
    'chromedriver_path': '/usr/local/share/chromedriver',
    'get_msg_interval': 2,  # Time (seconds). Recommended value: 5
    'colors': True,  # True/False. True prints colorful msgs in console
    'ww_url': "https://web.whatsapp.com/"
}

message_scheduler = sched.scheduler(time.time, time.sleep)
last_printed_msg_id = 0
last_thread_name = ''

# colors in console
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    def main():
        # setting up Chrome with selenium
        driver = webdriver.Chrome(config['chromedriver_path'])
        
        # open WW in browser
        driver.get(config['ww_url'])
        
        # prompt user to connect device to WW
        while True:
            isConnected = input(decorateMsg("\n\tPhone connected? y/n: ", bcolors.HEADER))
            if isConnected.lower() == 'y':
                break

            assert "WhatsApp" in driver.title

        # start background thread
        message_thread = threading.Thread(target=startGetMessages, args=(driver,))
        message_thread.start()

        while True:
            pass
    
    def sendMessage(driver, msg):
        """
        Type 'msg' in 'driver' and press RETURN
        """
        # select correct input box to type msg
        input_box = driver.find_element(By.XPATH, '//*[@id="main"]//footer//div[contains(@class, "input")]')
        # input_box.clear()
        input_box.click()

        action = ActionChains(driver)
        action.send_keys(msg)
        action.send_keys(Keys.RETURN)
        action.perform()
        return True

    def startGetMessages(driver):
        """
        Start schdeuler that gets messages every get_msg_interval seconds
        """
        message_scheduler.enter(config['get_msg_interval'], 1, getMessage, (driver, message_scheduler))
        message_scheduler.run()

    
    def getMessage(driver, scheduler):
        print("Getting Messages.")

        # Date and Time
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        # message variables.
        message_found = False
        sms_id = 0
        sms_category = ""
        sms_type = ""
        sms_receiver = ""
        sms_receiver_title = ""
        sms_body = ""
        sms_chat_found = ""
        sms_processed = 0
        sms_processed_at = ""
        sms_created_at = ""

        # Getting outbox message from API.
        #raw_messages = json.loads("http://192.168.0.53/ww-api/GetMessages.php")
        #messages = json.loads(raw_messages.decode("utf-8"))
        #print(messages)

        req = urllib2.Request("http://192.168.0.53/ww-api/GetMessages.php")
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = json.loads(f.read().decode('utf-8'))

        message = data['messages']
        print (message)

        # add the task to the scheduler again
        message_scheduler.enter(config['get_msg_interval'], 1, getMessage, (driver, scheduler,))

    def decorateMsg(msg, color=None):
        """
        Returns:
                colored msg, if colors are enabled in config and a color is provided for msg
                msg, otherwise
        """
        msg_string = msg
        if config['colors']:
            if color:
                msg_string = color + msg + bcolors.ENDC

        return msg_string
    
    def printThreadName(driver):
        global last_thread_name
        curr_thread_name = driver.find_element(By.XPATH, '//*[@id="main"]/header//div[contains(@class, "chat-main")]').text
        if curr_thread_name != last_thread_name:
            last_thread_name = curr_thread_name
            print(decorateMsg("\n\tSending msgs to:", bcolors.OKBLUE), curr_thread_name)
        return curr_thread_name
    
    def chooseReceiver(driver, receiver):
        friend_name = receiver
        input_box = driver.find_element(By.XPATH, '//*[@id="side"]//input')
        input_box.clear()
        input_box.click()
        input_box.send_keys(friend_name)
        input_box.send_keys(Keys.RETURN)
        printThreadName(driver)
        return True

    if __name__ == '__main__':
        main()

except AssertionError as e:
    sys.exit(decorateMsg("\n\tCannot open Whatsapp web URL.", bcolors.WARNING))

except KeyboardInterrupt as e:
    sys.exit(decorateMsg("\n\tPress Ctrl+C again to exit.", bcolors.WARNING))

except WebDriverException as e:
    sys.exit()