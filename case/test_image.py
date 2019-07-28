from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
time.sleep(2)
file_path = '../report/123' + '.png'
driver.save_screenshot(file_path)
time.sleep(2)

driver.quit()
