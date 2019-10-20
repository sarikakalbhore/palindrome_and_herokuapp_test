#SET PATH=c:\tmp\Python;c:\tmp\Python\Scripts;%PATH%

import selenium
from selenium import webdriver
import time
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(chrome_options=options)

# Maximize chrome window
driver.maximize_window()

# Open the url
driver.get('http://the-internet.herokuapp.com/')

# Click at "JavaScript Alerts"
driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[29]/a").click()

# Click at button "Click for JS Confirm"
driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[2]/button").click()

# Get the alert handle
alert = driver.switch_to.alert

# Sleep for 1 seconds to visualize the alert
time.sleep(1)

# Accept the alert
alert.accept()

# Get the message from the result 
message=driver.find_element_by_xpath("/html/body/div[2]/div/div/p[2]").text

# Validate the result text 
if message == "You clicked: Ok":
    print("Test Passed")
else :
    print("Test Failed")
    
# Close the chrome window
driver.close()
