from selenium import webdriver
import googlePage
import openLendingPage
import unittest

class OpenLending(unittest.TestCase):

    TIMEOUT = 30

    searchText = "Open Lending"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:\TestAutomation\ChromeDriver\chromedriver.exe')

    def setUp(self):
        self.google = googlePage.GooglePage(self, self.driver, self.TIMEOUT)
        self.openLending = openLendingPage.OpenLendingPage(self, self.driver, self.TIMEOUT)

    def test_open_lending(self):
        self.google.open_google()
        self.google.search(self.searchText)
        self.google.click_open_lending_link()
        self.openLending.open_resources()
        self.openLending.open_all_load_more_sections()
        blogs = self.openLending.get_all_blog_links()
        # Verify no duplicates
        self.assertTrue(len(set(blogs)) == len(blogs))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(catchbreak=True)
