import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# validate expected list with actual list
expectedlist = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actuallist =[]


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,'search-keyword').send_keys("ber")
time.sleep(2)#elements are more
results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    actuallist.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expectedlist == actuallist
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)    
assert sum == totalamount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
disamount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)  # discouted amount
print(disamount)
assert totalamount > disamount  #validated dicount price less than actual price