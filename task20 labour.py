import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"Downloads","download.directory_upgrade": True,"plugins.always_open_pdf_externally": True})
chromeOptions.set_capability("acceptInsecureCerts", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chromeOptions)
driver.get("https://labour.gov.in/")
driver.find_element(By.XPATH, "//button[normalize-space()='X']").click()
sleep(3)
actions = ActionChains(driver)
Docs=driver.find_element(By.XPATH, "//a[normalize-space()='Documents']")
actions.move_to_element(Docs).perform()
sleep(3)
Monthlyreport=driver.find_element(By.XPATH, "//a[normalize-space()='Monthly Progress Report']")
actions.move_to_element(Monthlyreport).click().perform()
sleep(3)
download=driver.find_element(By.XPATH,"//a[normalize-space()='Download(271.97 KB)']").click()
driver.switch_to.alert.accept()
time.sleep(10)
