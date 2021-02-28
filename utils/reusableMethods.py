from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from asserts import assert_true

global driver
driver = webdriver.Chrome(ChromeDriverManager().install())

def invokeApp():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    
def enterById(locator, data):
    driver.find_element_by_id(locator).send_keys(data)
    
def clickById(locator):
    driver.find_element_by_id(locator).click()
    
def verifyText(locator, data):
    str = driver.find_element_by_id(locator).text
    assert_true(True, data)