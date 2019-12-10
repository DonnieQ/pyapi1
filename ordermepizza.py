#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Student\Downloads\operadriver_win64\operadriver.exe")
driver.get("https://dominos.com/en/")

time.sleep(7)

click_delivery = driver.find_element_by_xpath('//*[@id="homeWrapper"]/main/section[1]/div/div[2]/a[2]')
click_delivery.click()

time.sleep(9)

# equivalent to left clicking on the text field
driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').click()
# fill in with zipcode
driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').send_keys('98499' + Keys.RETURN)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="locationsResultsPage"]/div/div[2]/div[1]/div[2]/div/div[2]/div/a').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="entree-Pizza"]/a/div[2]/h2').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[1]/div/a[1]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="orderSummaryInColumn"]/div[2]/div[1]/a').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="genericOverlay"]/section/div/div/div[2]/div/div[4]/a[2]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/a').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[5]/div/div[2]/div/div[4]/label/input').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[6]/div/div[3]/button').click()