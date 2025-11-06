from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    home = HomePage(driver)
    home.open_homepage()
    home.search_item("electronics")

    search = SearchResultsPage(driver)
    search.apply_filters()
    products = search.count_products()

    product = ProductPage(driver)
    product.open_first_product(products)
    product.verify_free_shipping()

finally:
    driver.quit()
