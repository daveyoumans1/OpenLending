from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = {
    "navbarToggler": (By.CSS_SELECTOR, "button.navbar-toggler"),
    "resourcesLink": (By.XPATH, "//li/a[contains(text(), 'Resources')]"),
    "loadingButton": (By.XPATH, "//button[contains(text(), 'Loading...')]"),
    "loadMoreButton": (By.CSS_SELECTOR, "button.facetwp-load-more"),
    "loadMoreButtonHidden": (By.CSS_SELECTOR, "button.facetwp-load-more.facetwp-hidden"),
    "genericBlogLink": (By.CSS_SELECTOR, "div.lenders-featured-block > a"),
    }

class OpenLendingPage:

    def __init__(self, testcase, driver, timeout):
        # Timeout value is in seconds
        self.testcase = testcase
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def ajax_wait(self):
        # Wait for all jQuery AJAX requests to finish.
        self.wait.until(lambda d: d.execute_script("return window.$.active == 0"))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # Need to scroll down 200px due to navbar at the top of the screen
        self.driver.execute_script("window.scrollBy(0, -200)")

    def open_resources(self):
        driver = self.driver
        driver.find_element(*locators["navbarToggler"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["resourcesLink"]))
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(*locators["resourcesLink"])).perform()
        driver.find_element(*locators["resourcesLink"]).click()

    def click_load_more_button(self):
        button = self.driver.find_element(*locators["loadMoreButton"])
        self.scroll_into_view(button)
        self.driver.find_element(*locators["loadMoreButton"]).click()
        self.ajax_wait()
        self.wait.until_not(EC.presence_of_element_located(locators["loadingButton"]))

    def open_all_load_more_sections(self):
        while self.driver.find_elements(*locators["loadMoreButton"]):
            self.click_load_more_button()
            if self.driver.find_elements(*locators["loadMoreButtonHidden"]):
                break

    def get_all_blog_links(self):
        blogLinks = []
        blogs = self.driver.find_elements(*locators["genericBlogLink"])
        for blog in blogs:
            blogLinks.append(blog.get_attribute("href"))
        return blogLinks
