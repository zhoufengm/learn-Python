'''
    LoginPage:登录页面对象，主要用于实现整个登录流程
'''
import os
import sys
path = os.getcwd()  # 获取当前文件目录
# sys.path.append(r'\AutoCode\learn-Python\learn_pom')
sys.path.append(path)

from base.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    # 元素
    username = (By.NAME,'accounts')
    password = (By.NAME,'pwd')
    login_btn = (By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    # 业务流程
    def login(self,usr,pwd):
        self.visit()
        self.input(self.username,usr)
        self.input(self.password,pwd)
        self.click(self.login_btn)

# # 调试代码
# if __name__ == '__main__':
#     driver =webdriver.Chrome()
#     usr = 'zzauto'
#     pwd = 'zz123456'
#     lp = LoginPage(driver)
#     lp.login(usr,pwd)
