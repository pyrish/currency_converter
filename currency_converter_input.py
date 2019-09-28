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

def extract_dropdown_items():
    select = Select(driver.find_element_by_id('sourceCurrency'))
    options = select.options
    options_list = []
    for option in options:
        options_list.append(option.get_attribute("value"))
    return(options_list)

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

    return(float(converted_amount))


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
  print('          Currency converter -  Mariano Vazquez, 2019'          )
  print('###############################################################')
  print('\n')
  print("Popular currencies: EUR | GBP | USD | INR | CAD | JPY | AUD | CHF")
  print('\n')

  currency_list = extract_dropdown_items()

  for i in range(1,6):

      source_amount = float(input("Please enter the amount #" + str(i) + " to be converted: "))
      while source_amount <= 0 or not source_amount:
          source_amount = float(input("Amount should be a positive number greater than zero, please enter again the amount #" + str(i) + " to be converted: "))

      from_currency = input("Please enter the source currency: ")
      while from_currency.upper().strip() not in currency_list:
          from_currency = input("Invalid source currency, please enter a valid source currency: ").strip()

      to_currency = input("Please enter the target currency: ").strip()

      while to_currency.upper().strip() not in currency_list:
          to_currency = input("Invalid target currency, please enter a valid target currency: ").strip()

      converted_amount = currency_iteration(url, source_amount, from_currency.upper(), to_currency.upper())

      print(">> " + str(source_amount) + " " + from_currency.upper() + " are equal to " + str(round(converted_amount, 2)) + " " + to_currency.upper())
      print('\n')

  driver.close()