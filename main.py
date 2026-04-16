from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Service (fix path)
service = Service(r'chromedriver-win64\chromedriver.exe')

# Driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open website
driver.get('https://demoqa.com/login')

wait = WebDriverWait(driver, 10)

# Locate elements
username_field = wait.until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
#login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login')))
login_button = driver.find_element(By.ID, 'login')
#login_button.click()

# Send data
username_field.send_keys('bjaiswal')
password_field.send_keys('Gen@20081981')
driver.execute_script("arguments[0].click();", login_button)

input("Press Enter to close the browser...")

driver.quit()