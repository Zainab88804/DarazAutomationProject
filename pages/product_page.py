from selenium.webdriver.common.by import By
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def open_first_product(self, products):
        # Open first product
        products[0].click()
        print("✅ Opened first product.")
        time.sleep(5)

    def verify_free_shipping(self):
        # Check if "Free Shipping" is visible
        time.sleep(2)
        elements = self.driver.find_elements(By.XPATH, "//span[contains(., 'Free Shipping')]")
        if len(elements) > 0:
            print("✅ Free shipping is available!")
        else:
            print("🚫 Free shipping not available.")
