from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

locators = {
    "googleTextField": (By.CSS_SELECTOR, "#APjFqb"),
    "openLendingLink": (By.XPATH, "//h3[contains(text(), 'Automated Lending Platform | Open Lending | United States')]"),
    }

class GooglePage:

    def __init__(self, testcase, driver, timeout):
        # timeout value is in seconds
        self.testcase = testcase
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def wait_for_page_to_load(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState == 'complete'"))

    def open_google(self):
        self.driver.get("http://www.google.com/")
        self.wait_for_page_to_load()
        self.wait.until(EC.visibility_of_element_located(locators["googleTextField"]))

    def search(self, searchText):
        self.driver.find_element(*locators["googleTextField"]).send_keys(searchText)
        self.driver.find_element(*locators["googleTextField"]).send_keys(Keys.ENTER)
        self.wait_for_page_to_load()
        self.wait.until(EC.visibility_of_element_located(locators["openLendingLink"]))

    def click_open_lending_link(self):
        self.driver.find_element(*locators["openLendingLink"]).click()
        self.wait_for_page_to_load()
