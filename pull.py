from selenium import webdriver  
# To perform automated user actions, we need a dedicated library for the respective browser
# In this case, we use webdriver library for chrome

driver = webdriver.Chrome()
# Note: You need a chromedriver exe along with webdriver for this to work