from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 

# driver = webdriver.Chrome(ChromeDriverManager().install())

# AjtLy _1FXE6 _1lF7t

driver = webdriver.Chrome("D:\\Visual Studio Code\\automation_wp_msg\\test\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")

time.sleep(15)

content = driver.find_element(By.CLASS_NAME, "AjtLy _1FXE6 _1lF7t")

print(content)