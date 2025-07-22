import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Use fixed name
name = "Maxwell"

# Generate random email
random_number = str(random.randint(1000, 9999))
random_email = f"santoz{random_number}@yopmail.com"

print(f"Using name     : {name}")
print(f"Generated email: {random_email}")

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")

# Click 'Signup / Login'
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Signup / Login')]"))
).click()

# Fill signup form (name and email)
driver.find_element(By.NAME, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(random_email)
driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()

# Wait for registration form to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_gender1"))
)

# Fill account info
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "password").send_keys("Akuntes1.")
driver.find_element(By.ID, "days").send_keys("10")
driver.find_element(By.ID, "months").send_keys("June")
driver.find_element(By.ID, "years").send_keys("1995")
driver.find_element(By.ID, "newsletter").click()
driver.find_element(By.ID, "optin").click()

# Fill address info
driver.find_element(By.ID, "first_name").send_keys(name)
driver.find_element(By.ID, "last_name").send_keys("Paldowski")
driver.find_element(By.ID, "company").send_keys("PT Exercise Python")
driver.find_element(By.ID, "address1").send_keys("Jl. Captain Pierre Tendean No. 1")
driver.find_element(By.ID, "address2").send_keys("Griya Residence")
driver.find_element(By.ID, "country").send_keys("United States")
driver.find_element(By.ID, "state").send_keys("Indonesia")
driver.find_element(By.ID, "city").send_keys("Yogyakarta")
driver.find_element(By.ID, "zipcode").send_keys("90001")
driver.find_element(By.ID, "mobile_number").send_keys("085793357797")

# Submit registration
driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()

# Verify account creation
success_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//b[contains(text(),'Account Created!')]"))
)
assert success_text.is_displayed(), "\033[91m Account creation failed! \033[0m"
print("\033[92m Account created successfully! \033[0m")

# Click 'Continue'
driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()

# Logout
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]"))
).click()

# Login with the newly created account
driver.find_element(By.NAME, "email").send_keys(random_email)
driver.find_element(By.NAME, "password").send_keys("Akuntes1.")
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

# Verify login success
logged_in_as = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
)
assert name in logged_in_as.text, f"\033[91m Login failed or name mismatch! Expected: {name} \033[0m"
print(f"\033[92m Login successful as {name}! \033[0m")

# Pause before closing
time.sleep(3)

# Quit browser
driver.quit()
