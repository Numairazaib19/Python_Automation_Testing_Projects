# Amazon Search Test using Selenium WebDriver

This project is a Python script that utilizes Selenium WebDriver to perform a search on the Amazon website and verify if a specific product is present in the search results.

## Prerequisites

Before running the script, make sure you have the following components installed on your system:

1. Python 3.x (https://www.python.org/)
2. Chrome WebDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Installation

1. Install the required Python packages using pip:
   ```
   pip install selenium
   ```

## Usage

1. Open the `amazon_search_test.py` file and edit the `search_query` variable in the main function. Set it to the product you want to search for on Amazon.

2. Save the changes.

3. Open your terminal or command prompt and navigate to the directory where the `amazon_search_test.py` file is located.

4. Execute the script:
   ```
   python amazon_search_test.py
   ```

The script will open a Chrome browser window and perform the following steps:

1. Navigate to the Amazon website.

2. Enter the specified `search_query` in the search box and submit the search.

3. Wait for the search results page to load.

4. Check if the expected product, defined by the `expected_product` variable, is present in the search results.

5. Print a success message if the product is found, or a failure message if it is not found.

6. Close the Chrome browser after the test is complete.

## Note

Please make sure to replace `'./chromedriver'` in the script with the actual path to your Chrome WebDriver executable.


