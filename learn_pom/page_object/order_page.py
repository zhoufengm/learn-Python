'''
    OrderPage:商品详情页下单的页面对象，主要用于实现整个下单流程
'''
import os
import sys
path = os.getcwd()  # 获取当前文件目录
# sys.path.append(r'\AutoCode\learn-Python\learn_pom')
sys.path.append(path)

from base.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html'

    # 元素
    suit = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[1]')
    color = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[1]/img')
    disk = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[3]')
    order_btn = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button')

    # 业务流程
    def order(self):
        self.visit()
        self.click(self.suit)
        self.wait(1)
        self.click(self.color)
        self.wait(1)
        self.click(self.disk)
        self.wait(1)
        self.click(self.order_btn)

# # 调试代码
# if __name__ == '__main__':
#     driver =webdriver.Chrome()
#     usr = 'zzauto'
#     pwd = 'zz123456'
#     lp = LoginPage(driver)
#     lp.login(usr,pwd)
