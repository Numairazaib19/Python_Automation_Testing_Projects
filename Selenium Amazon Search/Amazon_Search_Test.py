# Import the required modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define a function to perform the Amazon search test
def amazon_search_test(search_query):
    
    driver = webdriver.Chrome(executable_path='./chromedriver')
    
    try:
        # Step 1: Navigate to Amazon website
        driver.get('https://www.amazon.com/')
        
        # Step 2: Find the search box, enter the search query, and submit the form
        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
        
        # Step 3: Wait for the search results page to load and find the search result element
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))
        
        # Step 4: Check if the expected product is present in the search results
        expected_product = "OtterBox Galaxy S23 Commuter Series Case - BLACK, slim & tough, pocket-friendly, with port protection"  # Replace with the product name you expect to find
        search_results = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        
        for result in search_results:
            if expected_product in result.text:
                # If the expected product is found, print a success message
                print(f"Test Passed! Found the product: {expected_product}")
                break
        else:
            # If the expected product is not found, print a failure message
            print(f"Test Failed! Product '{expected_product}' not found in search results.")
        
    finally:
        # Quit the WebDriver after the test is complete
        driver.quit()

# Main function
if __name__ == "__main__":
    # Set the search query to "Mobile case" (you can change this to the product you want to search for)
    search_query = "Mobile case"  # Change this to the product you want to search for
    # Call the amazon_search_test function with the given search query
    amazon_search_test(search_query)
