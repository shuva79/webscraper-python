from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://tms07.nepsetms.com.np/tms/client/dashboard'


driver = webdriver.Chrome('./chromedriver')
driver.get(url)

time.sleep(100)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
whole_table = soup.find('div', attrs= {"class" : "numeric"})
table_data = whole_table.find_all('tr')

i = 0
for data in table_data:
    print(data[i])
    i+=1