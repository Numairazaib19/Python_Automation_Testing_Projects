# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver using the chromedriver executable located in the current directory
driver = webdriver.Chrome('./chromedriver')

# Open the Facebook login page in the browser
driver.get("http://www.facebook.com")

# Print the title of the current page (should be "Facebook" in this case)
print(driver.title)

# Locate the email input field on the page using its ID and store it in the 'username' variable
username = driver.find_element(By.ID, "email")

# Clear any existing text in the email input field
username.clear()

# Enter the email address into the email input field
username.send_keys("Email")

# Locate the password input field on the page using its ID and store it in the 'password' variable
password = driver.find_element(By.ID, "pass")

# Clear any existing text in the password input field
password.clear()

# Enter the password into the password input field
password.send_keys("Password")

# Simulate pressing the Enter key to submit the login form
password.send_keys(Keys.RETURN)

# Wait for 10 seconds to give the browser time to log in and load the next page
time.sleep(10)

# Print the current URL of the page (should be the URL after successful login)
print(driver.current_url)

# Close the browser and terminate the WebDriver session
driver.close()