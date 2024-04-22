from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys("sairam")
try:
    confirm_password_input = driver.find_element(By.XPATH, "//input[@id='confirmPassword']")
except NoSuchElementException:
    print("Element not found. Check your XPath or timing.")
#driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys("sairam")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
