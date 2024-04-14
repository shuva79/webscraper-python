from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import ast
import math


# Importing local files
from local_time import local_time


# Launches chrome driver
driver = webdriver.Chrome()

print(local_time())

# Navigates to the login page
driver.get("https://tms07.nepsetms.com.np/login")


# Locate username and password form elements
uname = driver.find_element(By.XPATH, "//input[@placeholder = 'Client Code/ User Name']")
pword = driver.find_element(By.ID,"password-field")

# Enter login details
uname.send_keys("")     # Enter username here 
pword.send_keys("")     # Enter password here

# Delay to enter captcha
time.sleep(5)

# Automatically presses login
pword.send_keys(Keys.RETURN)

# Wait for page to load again and then do the task below
# work still in progress in this one
driver.implicitly_wait(5)

# Manually go to ordermanagement > buy/sell
# This enters the scrip name automatically
order_mgmt = driver.find_element(By.XPATH, "//input[@typeaheadoptionfield = 'symbolName']")

# This is to enter scrip name
def scrip_name():
    # Edit the scrip name here
    order_mgmt.send_keys("ANLB")

    # Delay time and then enter the key name.
    time.sleep(0.5)
    order_mgmt.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

scrip_name()

# This is to click buy button in buy/sell
def buy_btn_click():
    buy_button = driver.find_element(By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[1]/div[2]/app-three-state-toggle/div/div/label[3]")
    buy_button.click()

buy_btn_click()

# This is to place quantity order
def place_qty_num():
    qty_num = driver.find_element(By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[3]/input")
    qty_num.send_keys("15")


# This is to place price 
def place_price_num(set_price):
    price_num = driver.find_element(By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input")
    price_num.send_keys(set_price)

# This clicks the buy button
def buy_shares():
    buy_stonks = driver.find_element(By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[2]/button[1]")
    buy_stonks.click()

# Pulling the actual data using data element
def latest_price():
    # Waiting for the angular content to load to be located
    wait = WebDriverWait(driver, 4.5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[1]")))

    # Find the element that contains the data 
    element = driver.find_element(By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[1]")
    data = element.text

    # Strips the ltp and change thingy and gives us the final data
    stripped_data = data.strip('LTP').strip()
    # Strips the point change portion by stripping text upon encountering space
    ltp = stripped_data.split()[0]
    return ast.literal_eval(ltp)

print(latest_price())
# Logic still in progress
ltp_initial = latest_price()
count = 0
while local_time() < "15:00:00":

    time.sleep(0.01)
    ltp_copy = latest_price()

    if ltp_copy != ltp_initial:
        ltp_initial = ltp_copy
        set_price = math.floor(((ltp_initial + 0.02*(ltp_initial))*10))/10
        

        # Set price and quantity (qty is set to 10 and price is update regularly)
        place_qty_num()
        place_price_num(set_price)
        time.sleep(0.5)
        # Place actual buy order
        buy_shares()
        
        driver.implicitly_wait(4)
        # Does same thing as buy_btn_click() but the function doesn't work for some reason
        buy_button = driver.find_element(By.XPATH, "/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[1]/div[2]/app-three-state-toggle/div/div/label[3]")
        buy_button.click()

        print(f"Success, changed at {local_time()}")
        print(set_price)
        print(ltp_initial)
        
       
        
     


# Wait for the page to load
# Explained further in obsidian(Automated login window)
driver.implicitly_wait(10)


time.sleep(5)
driver.quit()