from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.brand_filter = (By.XPATH, "//span[contains(text(), 'Samsung')]")
        self.price_section = (By.XPATH, "//span[contains(text(), 'Price')]")
        self.min_price = (By.XPATH, "//input[contains(@placeholder, 'Min')]")
        self.max_price = (By.XPATH, "//input[contains(@placeholder, 'Max')]")
        self.apply_price_btn = (By.XPATH, "//button[contains(text(), 'Apply')]")
        self.products = (By.XPATH, "//div[contains(@data-qa-locator, 'product-item')]")

    def apply_filters(self):
        """Apply brand and price filters"""
        wait = WebDriverWait(self.driver, 10)
        try:
            # Wait and click brand filter
            brand = wait.until(EC.element_to_be_clickable(self.brand_filter))
            self.driver.execute_script("arguments[0].click();", brand)
            time.sleep(3)

            # Click Price section to open the filter fields
            price_section = wait.until(EC.element_to_be_clickable(self.price_section))
            self.driver.execute_script("arguments[0].click();", price_section)
            time.sleep(2)

            # Enter price range
            min_input = wait.until(EC.presence_of_element_located(self.min_price))
            max_input = wait.until(EC.presence_of_element_located(self.max_price))
            min_input.clear()
            min_input.send_keys("500")
            max_input.clear()
            max_input.send_keys("5000")

            # Apply filter
            apply_btn = wait.until(EC.element_to_be_clickable(self.apply_price_btn))
            self.driver.execute_script("arguments[0].click();", apply_btn)
            time.sleep(3)

        except Exception as e:
            print("Filter apply error:", e)

    def count_products(self):
        """Count visible products"""
        time.sleep(3)
        items = self.driver.find_elements(*self.products)
        print("Total products found:", len(items))
        if len(items) > 0:
            print("✅ Products found successfully")
        else:
            print("❌ No products found")
        return items
