from selenium import webdriver
from . import request as req

driver = webdriver.Chrome()
driver.get(url=req.ask_url)
driver.save_screenshot("screenshot.png")
driver.quit()