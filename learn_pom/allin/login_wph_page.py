'''
    LoginPage:登录页面对象，主要用于实现整个登录流程
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    # url
    url = 'https://passport.vip.com/login?src=https%3A%2F%2Fwww.vip.com%2F'

    # 元素
    pwd_pancel = (By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div[2]')
    username = (By.ID,'J_login_name')
    password = (By.ID,'J_login_pwd')
    agree_btn = (By.XPATH,'//*[@id="J_login_form"]/div[6]/div[1]/div[1]/label')
    login_btn = (By.ID,'J_login_submit')

    # 业务流程
    def login(self,usr,pwd):
        self.visit()
        self.click(self.pwd_pancel)
        self.input(self.username,usr)
        self.input(self.password,pwd)
        self.click(self.agree_btn)
        self.click(self.login_btn)

# # 调试代码
# if __name__ == '__main__':
#     driver =webdriver.Chrome()
#     usr = '15980983306'
#     pwd = 'zfm021588'
#     lp = LoginPage(driver)
#     lp.login(usr,pwd)
