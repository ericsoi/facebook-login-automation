from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

# Replace these with your Twitter login credentials
username = "your_facebook_username"
password = "your_facebook_password"
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
time.sleep(30)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# Wait for a few seconds to let the login process complete
time.sleep(20)

# Close the browser 
# driver.quit()
