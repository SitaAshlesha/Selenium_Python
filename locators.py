from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.NAME,"email").send_keys("ashlesha.sonar@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("sairam")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.NAME,"name").send_keys("Ashlesha")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH,"(//input[@type='text']) [3]").send_keys("Ashlesha")
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "success" in message