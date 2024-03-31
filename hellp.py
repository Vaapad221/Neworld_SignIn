from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service  
import time  
import json  
import os  
  
# 创建 Chrome 选项对象  
chrome_options = Options()  
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--window-size=1420,1080')  
chrome_options.add_argument('--headless')  # 如果你不需要看到浏览器界面，使用无头模式  
chrome_options.add_argument('--disable-gpu')  
  
# 创建 Service 对象，并指定 chromedriver 的路径  
s = Service('/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')  
  
# 使用 Options 对象和 Service 对象初始化 webdriver.Chrome  
driver = webdriver.Chrome(service=s, options=chrome_options)  
  
# 现在你可以使用 driver 对象了  
# ...  
  
# 结束时记得关闭浏览器  
driver.quit()
  

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
driver.find_element_by_id('email').clear()
driver.find_element_by_id("email").send_keys(u)

driver.find_element_by_id('passwd').clear()
driver.find_element_by_id("passwd").send_keys(p)

time.sleep(1)
driver.find_element_by_id("login").click()

driver.refresh()#刷新页面 


driver.refresh()#刷新页面 

# time.sleep(5)

# buttons = driver.find_element_by_xpath("//button[@id='checkin']")
# print('buttons',buttons)

driver.find_element_by_id("checkin").click() # 点击元素
