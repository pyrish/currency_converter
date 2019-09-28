# Currency Converter Automation Script

Automation script developed in Python 3 with Selenium Webdriver.

![picture alt](https://github.com/pyrish/currency_converter/blob/master/currency_converter.png?raw=true"currency_converter.py")

## Requirements

Requirements (on your system)
1. Chrome/Chromium Browser (https://www.google.com/chrome/browser)
2. Chrome WebDriver (https://chromedriver.storage.googleapis.com/index.html)
3. Python3 (https://www.python.org/downloads/)
4. Virtualenv  - ```$ pip3 install virtualenv``` - Optional
5. Selenium - ```$ pip3 install selenium```

## Steps to run in your local machine

1. Firstly, clone the repository using the git shell <br/>```$ git clone https://github.com/pyrish/currency_converter.git```
2. Go to the base directory of the project  <br/>```$ cd currency-converter```
3. Install the requirements for the project  <br/> ```$ pip install -r requirements.txt```
5. Download the Chrome Webdriver (according to the version of your Chrome browser) and extract into the directory where you saved/cloned the currency_converter.py script.
6. In the file "currency_converter.py" replace "CHROME_PATH" variable with the absolute path of the downloaded Chrome Webdriver.
7. Run the script $ python3 currency_converter.py
8. Enter the details asked (amount, source currency, target currency)
9. Voila!

## Usage

```python
python3 currency_converter.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
