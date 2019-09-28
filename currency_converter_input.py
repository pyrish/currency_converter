# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import random


def clear_amount_field():
    amount_field = driver.find_element_by_id("cc-amount")
    amount_field.clear()


def currency_iteration(url, source_amount, from_currency, to_currency):
    wait = WebDriverWait(driver, 5)
    amount = wait.until(EC.visibility_of_element_located((By.ID, "cc-amount")))
    clear_amount_field()
    amount.click()
    amount.send_keys(str(source_amount))

    select_source = Select(driver.find_element_by_id('sourceCurrency'))
    select_source.select_by_value(from_currency)

    select_target = Select(driver.find_element_by_id('targetCurrency'))
    select_target.select_by_value(to_currency)

    convert_button = driver.find_element(By.ID,"convert").click()
    converted_currency = wait.until(EC.visibility_of_element_located((By.ID, "cc-amount-to")))
    converted_amount = driver.find_element_by_id("cc-amount-to").get_attribute('value')
    driver.back()

    return(converted_amount)


if __name__ == '__main__':

  #Options for Local box
  chrome_options = webdriver.ChromeOptions()
  chrome_driver_path = '/Users/mariano/Desktop/scrapers/chromedriver'
  driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

  url = 'https://transferwise.com/ie/currency-converter/'
  driver.get(url)

  os.system('clear')

  print('\n')
  print('###############################################################')
  print('       Currency converter script -  Mariano Vazquez, 2019'      )
  print('###############################################################')
  print('\n')

  for i in range(1,6):
      source_amount = input("Please enter the amount #" + str(i) + " to be converted: ")
      from_currency = input("Please enter the source currency: ")
      to_currency = input("Please enter the target currency: ")
      converted_amount = currency_iteration(url, source_amount, from_currency, to_currency)
      print(">> " + str(source_amount) + " " + from_currency + " are equal to " + str(converted_amount) + " " + to_currency)
      print('\n')

  driver.close()