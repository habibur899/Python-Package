import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


def get_chromedriver_path():
    """Return absolute path to chromedriver.exe located in the project root.
    If not found, returns None.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, "chromedriver.exe")
    if os.path.isfile(candidate):
        return candidate
    return None


def main():
    chromedriver_path = get_chromedriver_path()
    if chromedriver_path is None:
        print("Error: chromedriver.exe not found in the project directory.")
        print("Place chromedriver.exe next to main.py or update the path in get_chromedriver_path().")
        sys.exit(1)

    options = Options()
    # Keep default visible browser; set page load strategy as requested
    options.page_load_strategy = 'normal'

    service = Service(executable_path=chromedriver_path)

    try:
        driver = webdriver.Chrome(service=service, options=options)
    except WebDriverException as e:
        print(f"Failed to start Chrome WebDriver: {e}")
        print("Check that the chromedriver version matches your Chrome browser.")
        sys.exit(1)

    try:
        driver.get("https://www.facebook.com")
        # Let the page load and observe it for 10 seconds
        time.sleep(10)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
