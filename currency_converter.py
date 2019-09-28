#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python script using Selenium Webdriver to calculate the
    conversion rate of a given amount, selecting the source and
    target currencies. All these variables are provided by the user.
    All data has been validated accordingly"""

__author__ = "Mariano Vazquez"
__version__ = "1.0"
__email__ = "mariano.vazquez@live.com"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import platform # For getting the operating system name
import subprocess # For executing a shell command
import os

CHROME_PATH = '../chromedriver' # Path to folder where repo has been cloned or where Chromedriver has been downloaded to
URL = 'https://transferwise.com/ie/currency-converter/'
AMOUNT_FIELD = 'cc-amount'
SOURCE_CURRENCY = 'sourceCurrency'
TARGET_CURRENCY = 'targetCurrency'
CONVERTED_CURRENCY = 'cc-amount-to'

def clear_screen():
    if platform.system().lower() == "windows":
        command = "cls"
    else:
        command = "clear"
    return(subprocess.call(command) == 0)

def clear_amount_field():
    amount_field = driver.find_element_by_id(AMOUNT_FIELD)
    amount_field.clear()

def extract_dropdown_items():
    select = Select(driver.find_element_by_id(SOURCE_CURRENCY))
    options = select.options
    options_list = []
    for option in options:
        options_list.append(option.get_attribute("value"))
    return(options_list)

def currency_iteration(url, source_amount, from_currency, to_currency):
    wait = WebDriverWait(driver, 5)
    amount = wait.until(EC.visibility_of_element_located((By.ID, AMOUNT_FIELD)))
    clear_amount_field()
    amount.click()
    amount.send_keys(str(source_amount))

    select_source = Select(driver.find_element_by_id(SOURCE_CURRENCY))
    select_source.select_by_value(from_currency)

    select_target = Select(driver.find_element_by_id(TARGET_CURRENCY))
    select_target.select_by_value(to_currency)

    convert_button = driver.find_element(By.ID,"convert").click()
    converted_currency = wait.until(EC.visibility_of_element_located((By.ID, CONVERTED_CURRENCY)))
    converted_amount = driver.find_element_by_id(CONVERTED_CURRENCY).get_attribute('value')
    driver.back()

    return(float(converted_amount))


if __name__ == '__main__':

  driver = webdriver.Chrome(executable_path=CHROME_PATH)

  driver.get(URL)

  clear_screen()

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

      converted_amount = currency_iteration(URL, source_amount, from_currency.upper(), to_currency.upper())

      print(">> " + str(source_amount) + " " + from_currency.upper() + " are equal to " + str(round(converted_amount, 2)) + " " + to_currency.upper())
      print('\n')

print('Thank you for using the currency converted tool. Enjoy your day, Bye!')
print('\n')
driver.close()