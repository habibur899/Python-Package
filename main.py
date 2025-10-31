import os
import subprocess
import sys

import time
from selenium import webdriver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("https://www.facebook.com")
time.sleep(10)
driver.quit()

