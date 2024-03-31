from selenium import webdriver  
from selenium.webdriver.common.by import By
import time
import json
import os
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service  
  
# ChromeDriver 路径  
chromedriver_path = '/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver'  
  
# 创建 Chrome 选项对象  
chrome_options = Options()  
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--window-size=1420,1080')  
chrome_options.add_argument('--headless')  # 无头模式  
chrome_options.add_argument('--disable-gpu')  
  
# 创建 Service 对象，并指定 chromedriver 的路径  
s = Service(chromedriver_path)  
  
# 使用 Options 对象和 Service 对象初始化 webdriver.Chrome  
driver = webdriver.Chrome(service=s, options=chrome_options)  
  
# 现在你可以使用 driver 对象来执行你的自动化任务了  
# 例如，打开网页  


# driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')    # Chrome浏览器  

# windows 系统驱动路径
# driver = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe')    # Chrome浏览器


# 环境变量中读取数据，包含账号密码，和登陆页面测试
u = os.environ["USERNAME"]
p = os.environ["PASSWORD"]

print('u',u)
print('p',p)
driver.get("https://neworld.tv/auth/login") 
#  获取cookies 
time.sleep(5)
# 账号密码登录版本
# 使用新的方法查找元素并清除其内容  
driver.find_element(By.ID, 'email').clear()  
driver.find_element(By.ID, 'email').send_keys(u)

driver.find_element(By.ID, 'passwd').clear()
driver.find_element(By.ID, 'passwd').send_keys(p)

time.sleep(1)
driver.find_element(By.ID, 'login-dashboard').click()

driver.refresh()#刷新页面 


driver.refresh()#刷新页面 

# time.sleep(5)

# buttons = driver.find_element_by_xpath("//button[@id='checkin']")
# print('buttons',buttons)

driver.find_element(By.ID, 'checkin').click() # 点击元素
