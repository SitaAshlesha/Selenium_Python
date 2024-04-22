from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        print("radiobutton is selected",radiobutton.is_selected())
        break