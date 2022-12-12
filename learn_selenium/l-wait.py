from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

# 定义一个webdriver对象
driver = webdriver.Chrome()

# 2、隐式等待3秒，全局等待，所有用例执行都有等待
# driver.implicitly_wait(3)

# 访问百度
driver.get('http://www.baidu.com')

# 找到输入框元素，输入xuzhu
driver.find_element(By.ID,'kw').send_keys('xuzhu')

# 找到百度一下元素，点击
driver.find_element(By.ID,'su').click()

# 1、强制等待3秒
# sleep(3)

# 3、显示等待,10秒内按每1秒一次检查是否出现指定元素，出现则进行下一步
WebDriverWait(driver,10,1).until(lambda el:driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/h3/a'))

# 点击第一条搜索结果
driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/h3/a').click()

