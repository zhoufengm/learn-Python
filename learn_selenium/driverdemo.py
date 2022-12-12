from selenium.webdriver.common.by import By


# 常用方法：
# 创建一个浏览器对象
# from selenium import webdriver
# driver = webdriver.Chrome()
# #浏览器访问指定的URL
# driver.get('http://www.baidu.com')
# 元素的定位：获取WebElement
# el1 = driver.find_element(By.ID,'kw').send_keys('测码学院')
# el11 = driver.find_element(By.ID,'su').click()
# print(type(el1))
# print(el1)

# 实际底层代码调用方法：
from selenium.webdriver.chrome.webdriver import WebDriver
wb = WebDriver(executable_path="chromedriver")
#浏览器访问指定的URL
wb.execute('get',{'url':'http://www.baidu.com'})
el2 = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//*[@id="kw"]'
})['value']
print(type(el2))
print(el2)
el2._execute('sendKeysToElement',  {'text': '虚竹',
                                    'value': ''}) #value可以为空
el22 = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//*[@id="su"]'
})['value']
el22._execute('clickElement')