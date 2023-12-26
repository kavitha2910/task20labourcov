import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.cowin.gov.in/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//a[normalize-space()='FAQ']").click()
sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Partners']").click()
sleep(5)
windowids=driver.window_handles
faqwindowid1=windowids[1]
partnerwindowid2=windowids[2]
print(faqwindowid1)
print(partnerwindowid2)
time.sleep(3)
driver.close()