from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(10)  # Adding a wait time, e.g., 10 seconds

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")  # Added a closing parenthesis

for product in products:
    name = product.find_element(By.XPATH, "div/h4/a").text
    if name == "Blackberry":  # Fixed comparison operator
        product.find_element(By.XPATH, "div/button").click()  # Added a closing parenthesis

driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
assert "Success! Thank you" in message
driver.close()



