import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Initialize a new instance of the Chrome driver
driver = webdriver.Chrome()
print(USERNAME)
print(PASSWORD)
try:
    # Open LinkedIn's login page
    driver.get("https://www.linkedin.com/login")

    # Find the email input field, enter your email, and press Enter
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(USERNAME)
    email_input.send_keys(Keys.RETURN)

    # Find the password input field, enter your password, and press Enter
    password_input = driver.find_element(By.ID, "password")
    print("password found:", password_input)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(20)
    # Wait for the Jobs link to be clickable and click it
    inner_text_jobs = "Jobs"
    xpath_expression_jobs = f"//*[text()='{inner_text_jobs}']"
    wait = WebDriverWait(driver, 10)
    link_jobs = wait.until(EC.element_to_be_clickable(
        (By.XPATH, xpath_expression_jobs)))
    link_jobs.click()

    # Find the Jobs input field and enter job title
    time.sleep(3)
    job_title_id = "jobs-search-box-keyword-id-ember"
    job_title = driver.find_element(By.CSS_SELECTOR, f"[id^='{job_title_id}']")

    job_title.send_keys("Developer")
    job_title.send_keys(Keys.RETURN)
    time.sleep(5)
    job_location_id = "jobs-search-box-location-id-ember"
    job_location = driver.find_element(
        By.CSS_SELECTOR, f"[id^='{job_location_id}']")

    job_location.send_keys("Minnesota")
    time.sleep(5)
    job_location.send_keys(Keys.RETURN)
    # Find the Locations input field, enter location, and press Enter
    # job_location_input = wait.until(EC.presence_of_element_located((By.ID, "location-typeahead-instance-ember22")))
    # job_location_input.send_keys("Minnesota")
    # job_location_input.send_keys(Keys.RETURN)

    # Wait
    time.sleep(120)

finally:
    # Close the browser window and perform cleanup
    driver.quit()
