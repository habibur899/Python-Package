import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def get_chromedriver_path():
    """Return absolute path to chromedriver.exe located in the project root.
    If not found, returns None.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, "chromedriver.exe")
    if os.path.isfile(candidate):
        return candidate
    return None


chromedriver_path = get_chromedriver_path()
options = Options()
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)


def facebook_account_create():
    fname = "Habib"
    lname = "Rahman"
    email = "email@gmail.com"
    password = "123456"
    driver.get("https://www.facebook.com/")
    # driver.find_element(By.NAME, "email").send_keys(email)
    # driver.find_element(By.NAME, "pass").send_keys(pwd)
    # button = driver.find_element(By.NAME, "login")
    # button.send_keys(Keys.ENTER)
    button = driver.find_element(By.LINK_TEXT, "Create new account")
    button.send_keys(Keys.ENTER)
    driver.find_element(By.NAME, "firstname").send_keys(fname)
    driver.find_element(By.NAME, "lastname").send_keys(lname)
    day_select = Select(driver.find_element(By.NAME, "birthday_day"))
    month_select = Select(driver.find_element(By.NAME, "birthday_month"))
    year_select = Select(driver.find_element(By.NAME, "birthday_year"))
    day_select.select_by_value("28")
    month_select.select_by_value("10")
    year_select.select_by_value("1990")
    male_checkbox = driver.find_element(By.XPATH, "//input[@name='sex' and @value='2']")
    male_checkbox.click()
    driver.find_element(By.NAME, "reg_email__").send_keys(email)
    driver.find_element(By.NAME, "reg_passwd__").send_keys(password)
    driver.find_element(By.NAME, "websubmit").click()

    time.sleep(5)
    driver.quit()


facebook_account_create()
