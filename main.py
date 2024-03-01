from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Launch the browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://xk.nju.edu.cn/xsxkapp/sys/xsxkapp/*default/grablessons.do?token=5eb0a055-c11c-46a0-9b0d-89980ae61753")

# Extract data
title = driver.title
url = driver.current_url
# content = driver.find_element_by_tag_name('body').text
login_name_element=driver.find_element(By.ID,"loginName")

login_pwd_element=driver.find_element(By.ID,"loginPwd")
login_name_element.send_keys("201180104")
login_pwd_element.send_keys("yzlsx20000")

print('Title:', title)
print('URL:', url)
# print('Content:', content)

# Close the browser
driver.close() 
