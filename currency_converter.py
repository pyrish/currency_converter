# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import random

#Options for Local box
chrome_options = webdriver.ChromeOptions()
chrome_driver_path = '/Users/mariano/Desktop/scrapers/chromedriver'
driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

url = 'https://transferwise.com/ie/currency-converter/'

def currency_iteration(source_amount, url):

    driver.get(url)

    source_c = ['USD', 'GBP', 'ARS', 'EUR', 'CAD']
    target_c = ['INR', 'AUD', 'MXN', 'JPY', 'NZD']

    for source in source_c:
        for target in target_c:
            wait = WebDriverWait(driver, 10)
            amount = wait.until(EC.visibility_of_element_located((By.ID, "cc-amount")))
            amount.click()
            amount.send_keys(str(source_amount))

            select_source = Select(driver.find_element_by_id('sourceCurrency'))
            select_source.select_by_value(source)

            select_target = Select(driver.find_element_by_id('targetCurrency'))
            select_target.select_by_value(target)

            convert_btn = driver.find_element(By.ID,"convert").click()

            converted_currency = wait.until(EC.visibility_of_element_located((By.ID, "cc-amount-to")))

            converted_amount = driver.find_element_by_id("cc-amount-to").get_attribute('value')

            print(str(source_amount) + " " + source + " are equal to " + str(converted_amount) + " " + target)

            driver.back()


if __name__ == '__main__':


  os.system('clear')

  source_amount = input("Enter the amount to calculate: ")

  currency_iteration(source_amount, url)
