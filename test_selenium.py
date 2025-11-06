from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")

# Chrome settings
options = Options()
options.add_experimental_option("detach", True)  # keeps Chrome open

# Open browser
driver = webdriver.Chrome(service=service, options=options)

# Go to Google
driver.get("https://www.google.com")

# Print page title
print("Page title is:", driver.title)
