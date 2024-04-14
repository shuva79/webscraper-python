from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Note to self: The problem as to why the error occurs could be because the website uses
# javascript and Beautiful soup is unable to handle javascript
# Ask sir if I should use selenium instead

url = 'https://tms07.nepsetms.com.np/tms/client/dashboard'

# This (headers) tells the website what browser and OS we're using
# Without headers, the program received a return code of 403 aka Access Forbidden
# 200 return code means you're good to get in
headers = {
    'User-Agent' : 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


dashboard = requests.get(url, headers=headers).text
soup = BeautifulSoup(dashboard, 'lxml')

whole_table = soup.find('div', attrs= {"class" : "order__form--prodtype price-display ng-star-inserted"})

print(whole_table)

table_body = whole_table.find('tbody')

rows = table_body.find_all('tr')


for row in rows:
    col = row.find_all('td')

     #strip() removes any trailing spaces from the data
     #ele 
    col = [ele.text.strip() for ele in col]    

    print(col)           
