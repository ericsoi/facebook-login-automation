from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

# Replace these with your Twitter login credentials
username = "ericksoi3709@gmail.com"
password = "Microsoft!@34"
service = Service()
options = webdriver.ChromeOptions()

# Path to the chromedriver executable (download and place it in the same directory as this script)
# chromedriver_path = "chromedriver"  # Update with the correct path for your system

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open Twitter's login page
driver.get("https://www.facebook.com/")

# Find the username and password input fields and fill them in
username_field = driver.find_element("name", "email")
username_field.send_keys(username)

password_field = driver.find_element("name", "pass")
password_field.send_keys(password)

# Press Enter to submit the form
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to let the login process complete
time.sleep(1000000)

# Close the browser
# driver.quit()
