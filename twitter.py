from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions
from selenium import webdriver

class Twitter:
    def __init__(self, executable_path, login, password):
        # URL for login page
        self.url = 'https://twitter.com/login'
        # User's login credentials
        self.login = login
        self.password = password
        # Create an instance of webdriver
        self.driver = webdriver.Edge(executable_path=executable_path)
        self.driver.get(self.url)

    def login(self):
        try:
            # Find the username input field
            xpath_username = '//input[@name="text"]'
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_username)))
            uid_input = self.driver.find_element_by_xpath(xpath_username)
            # Input the username and press Enter
            uid_input.send_keys(self.login)
            uid_input.send_keys(Keys.RETURN)
            # Find the password input field
            xpath_password = '//input[@name="password"]'
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_password)))
            pwd_input = self.driver.find_element_by_xpath(xpath_password)
            # Input the password and press Enter
            pwd_input.send_keys(self.password)
            pwd_input.send_keys(Keys.RETURN)
        except exceptions.TimeoutException:
            print("Timeout while waiting for Login screen")

    def home(self):
        try:
            # Navigate to home page
            self.driver.get('https://twitter.com/home')
            # Find the cards element
            xpath_cards = './/div[@data-testid="cellInnerDiv"]'
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_cards)))
            self.cards = self.driver.find_elements_by_xpath(xpath_cards)
        except exceptions.TimeoutException:
            print("Timeout while waiting for Home screen")
# Usage
executable_path = 'Your url'
login = "email"
password = "Your password"

twitter = Twitter(executable_path, login, password)
twitter.login()
twitter.home()
