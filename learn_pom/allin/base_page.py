'''
    基类：工具类，提供各个常用的已封装好的函数，便于后续的页面对象进行调用
'''

from selenium import webdriver
from time import sleep

class BasePage:
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self,driver):
        self.driver = driver

    # 访问URL
    def visit(self):
        self.driver.get(self.url)

    # 元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self,loc):
        self.locator(loc).click()

    # 等待
    def wait(self,time_):
        sleep(time_)

    # 关闭
    def quit(self):
        self.driver.quit()