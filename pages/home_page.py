from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "q")
        self.search_button = (By.CLASS_NAME, "search-box__button--1oH7")

    def open_homepage(self):
        """Open Daraz homepage"""
        self.driver.get("https://www.daraz.pk")
        self.driver.maximize_window()  # optional, better visibility

    def search_item(self, item):
        self.driver.find_element(*self.search_box).send_keys(item)
        self.driver.find_element(*self.search_button).click()
